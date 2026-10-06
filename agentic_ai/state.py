from typing import TypedDict, List, Dict, Optional


class PatientSummary(TypedDict, total=False):
    diagnosis: str
    previous_visit_outcome: str
    medications: List[str]
    next_steps: List[str]
    required_tests: List[str]
    follow_up_date: str
    important_concerns: List[str]
    case_severity: str


class PatientState(TypedDict, total=False):
    # -------------------------
    # Patient information
    # -------------------------
    patient_id: str
    patient_information: Dict

    # -------------------------
    # RAG / retrieved context
    # -------------------------
    retrieved_context: List[str]

    # -------------------------
    # Summary Agent
    # -------------------------
    patient_summary: PatientSummary

    # -------------------------
    # Reminder Agent
    # -------------------------
    reminder: Dict

    # -------------------------
    # Contact history
    # -------------------------
    contact_history: List[Dict]

    # -------------------------
    # Escalation Agent
    # -------------------------
    escalation: Dict

    # -------------------------
    # Human-in-the-loop
    # -------------------------
    human_decision: Optional[str]
    reviewer_comment: Optional[str]

    # -------------------------
    # Workflow control
    # -------------------------
    status: str
    errors: List[str]