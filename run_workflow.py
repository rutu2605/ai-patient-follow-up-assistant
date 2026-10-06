from agentic_ai.state import PatientState
from agentic_ai.workflow import build_workflow


def print_node_update(node_name: str, state: PatientState):
    print("\n" + "=" * 60)
    print(f"NODE COMPLETED: {node_name}")
    print("=" * 60)

    print("Status:", state.get("status"))

    if node_name == "summary_agent":
        print("\nPatient Summary:")
        for key, value in state.get("patient_summary", {}).items():
            print(f"  {key}: {value}")

    elif node_name == "reminder_agent":
        reminder = state.get("reminder", {})
        print("\nReminder:")
        print("  Subject:", reminder.get("subject"))
        print("  Priority:", reminder.get("priority"))
        print(
            "  Requires approval:",
            reminder.get("requires_approval")
        )

    elif node_name == "escalation_agent":
        print("\nEscalation:")
        for key, value in state.get("escalation", {}).items():
            print(f"  {key}: {value}")

    elif node_name == "human_approval":
        print("\nHuman Decision:")
        print(" ", state.get("human_decision"))


patient_state: PatientState = {
    "patient_id": "P001",

    "patient_information": {
        "name": "Rajesh Patel",
        "age": 58,
        "diagnosis": "Hypertension",

        "previous_visit_outcome": (
            "Blood pressure remained elevated during "
            "the previous consultation."
        ),

        "medications": [
            "Amlodipine 5 mg once daily"
        ],

        "next_steps": [
            "Continue prescribed medication",
            "Attend follow-up consultation"
        ],

        "required_tests": [
            "Blood pressure measurement",
            "Routine blood test"
        ],

        "follow_up_date": "2026-10-15",

        "important_concerns": [
            "Blood pressure remains elevated"
        ],

        "case_severity": "medium",
    },

    "retrieved_context": [
        "Discharge summary states that blood pressure "
        "remained elevated.",
        "Patient was instructed to complete a routine "
        "blood test before the follow-up."
    ],

    "patient_summary": {},
    "reminder": {},

    "contact_history": [
        {
            "date": "2026-10-10",
            "channel": "email",
            "status": "no_response",
        },
        {
            "date": "2026-10-12",
            "channel": "email",
            "status": "no_response",
        },
    ],

    "escalation": {},

    "human_decision": None,
    "reviewer_comment": None,

    "status": "started",
    "errors": [],
}


workflow = build_workflow()

print("\n" + "=" * 60)
print("CARELOOP AGENTIC WORKFLOW")
print("=" * 60)

print("\nInitial patient:", patient_state["patient_id"])
print("Starting workflow...")


# Stream the graph so we can see every node as it completes.
for event in workflow.stream(patient_state):

    for node_name, state_update in event.items():

        print_node_update(
            node_name,
            state_update
        )


print("\n" + "=" * 60)
print("WORKFLOW COMPLETE")
print("=" * 60)