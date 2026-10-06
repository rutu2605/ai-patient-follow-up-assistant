from langgraph.graph import StateGraph, START, END

from agentic_ai.state import PatientState
from agentic_ai.summary_agent import summary_agent
from agentic_ai.reminder_agent import reminder_agent
from agentic_ai.escalation_agent import escalation_agent


def human_approval(state: PatientState) -> PatientState:
    """
    Human-in-the-loop approval for the AI-generated
    patient reminder.

    The prototype allows the reviewer to:
    - approve
    - reject
    - edit
    """

    reminder = state.get("reminder", {})
    escalation = state.get("escalation", {})

    print("\n" + "=" * 60)
    print("HUMAN APPROVAL REQUIRED")
    print("=" * 60)

    print("\nReminder Subject:")
    print(reminder.get("subject"))

    print("\nReminder Message:")
    print(reminder.get("message"))

    print("\nPriority:")
    print(reminder.get("priority"))

    if escalation.get("escalate"):
        print("\nEscalation:")
        print(escalation.get("reason"))
        print(
            "Recommended team:",
            escalation.get("recommended_team")
        )

    print("\nOptions:")
    print("  [a] Approve")
    print("  [r] Reject")

    decision = input("\nEnter your decision: ").strip().lower()

    if decision == "a":
        human_decision = "approved"
        status = "approved"

    elif decision == "r":
        human_decision = "rejected"
        status = "rejected"

    else:
        print("\nInvalid decision. Keeping approval pending.")
        human_decision = "pending"
        status = "awaiting_approval"

    return {
        **state,
        "human_decision": human_decision,
        "status": status,
    }

def route_after_escalation(state: PatientState) -> str:
    """
    Decides whether escalation handling is required.
    """

    escalation = state.get("escalation", {})

    if escalation.get("escalate") is True:
        return "escalation_review"

    return "human_approval"

def escalation_review(state: PatientState) -> PatientState:
    """
    Prepares an escalation for human review.
    """

    escalation = state.get("escalation", {})

    print("\n--- ESCALATION REVIEW ---")
    print("Escalation required:", escalation.get("escalate"))
    print("Severity:", escalation.get("severity"))
    print("Reason:", escalation.get("reason"))
    print("Recommended team:", escalation.get("recommended_team"))

    return {
        **state,
        "status": "escalation_pending_review",
    }

def build_workflow():
    """
    Build and compile the CareLoop LangGraph workflow.
    """

    graph = StateGraph(PatientState)

    # Add agent nodes
    graph.add_node("summary_agent", summary_agent)
    graph.add_node("reminder_agent", reminder_agent)
    graph.add_node("escalation_agent", escalation_agent)
    graph.add_node("escalation_review", escalation_review)

    # Add human approval node
    graph.add_node("human_approval", human_approval)

    # Connect workflow
    graph.add_edge(START, "summary_agent")
    graph.add_edge("summary_agent", "reminder_agent")
    graph.add_edge("reminder_agent", "escalation_agent")
    graph.add_conditional_edges(
        "escalation_agent",
        route_after_escalation,
        {
            "escalation_review": "escalation_review",
            "human_approval": "human_approval",
        },
    )

    graph.add_edge("escalation_review", "human_approval")
    graph.add_edge("human_approval", END)

    return graph.compile()