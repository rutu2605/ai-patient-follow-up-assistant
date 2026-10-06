from agentic_ai.state import PatientState
from agentic_ai.summary_agent import summary_agent
from agentic_ai.reminder_agent import reminder_agent


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

    "contact_history": [],

    "escalation_required": False,
    "escalation_reason": None,

    "human_decision": None,
    "reviewer_comment": None,

    "status": "started",
    "errors": [],
}


# Step 1: Summary Agent
state_after_summary = summary_agent(patient_state)

# Step 2: Reminder Agent
state_after_reminder = reminder_agent(state_after_summary)


print("\n--- PATIENT SUMMARY ---")

for key, value in state_after_reminder["patient_summary"].items():
    print(f"{key}: {value}")


print("\n--- REMINDER ---")

reminder = state_after_reminder["reminder"]

print("Subject:", reminder["subject"])
print("Priority:", reminder["priority"])
print("Requires approval:", reminder["requires_approval"])

print("\nMessage:")
print(reminder["message"])


print("\n--- WORKFLOW STATUS ---")
print(state_after_reminder["status"])