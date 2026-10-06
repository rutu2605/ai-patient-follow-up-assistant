from state import PatientState


patient_state: PatientState = {
    "patient_id": "P001",

    "patient_information": {
        "name": "Rajesh Patel",
        "age": 58,
        "diagnosis": "Hypertension",
        "follow_up_date": "2026-10-15",
    },

    "retrieved_context": [
        "Patient was discharged after hypertension treatment.",
        "Blood test required before follow-up appointment.",
    ],

    "patient_summary": "",
    "reminder": "",

    "contact_history": [],

    "escalation_required": False,
    "escalation_reason": None,

    "human_decision": None,
    "reviewer_comment": None,

    "status": "started",
    "errors": [],
}


print("Patient ID:", patient_state["patient_id"])
print("Status:", patient_state["status"])
print("Patient information:", patient_state["patient_information"])
print("Retrieved context:", patient_state["retrieved_context"])