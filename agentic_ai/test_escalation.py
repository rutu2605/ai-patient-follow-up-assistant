from agentic_ai.state import PatientState
from agentic_ai.summary_agent import summary_agent
from agentic_ai.reminder_agent import reminder_agent
from agentic_ai.escalation_agent import escalation_agent


patient_state: PatientState = {
    "patient_id": "P001",

    "patient_information": {
        "name": "Rajesh Patel",
        "age": 58,
        "diagnosis": "Hypertension",

        "previous_visit_outcome": (
            "Blood pressure remained elevated."
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

        "case_severity": "high",
    },

    "retrieved_context": [
        "Discharge summary states that blood pressure "
        "remained elevated."
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


state = summary_agent(patient_state)
state = reminder_agent(state)
state = escalation_agent(state)


print("\n--- ESCALATION DECISION ---")

for key, value in state["escalation"].items():
    print(f"{key}: {value}")

print("\n--- WORKFLOW STATUS ---")
print(state["status"])