# AI Patient Follow-Up Assistant

An agentic AI system designed to help healthcare teams manage missed patient follow-ups through automated summarization, personalized reminders, escalation, and human approval.

> **Capstone Project — Agentic AI Component**

## Overview

Hospitals and healthcare teams can miss important patient follow-up communication because of high patient volumes and manual processes.

This project uses a **multi-agent workflow** to analyze patient information, generate personalized follow-up reminders, identify cases requiring escalation, and keep a human reviewer in control before any reminder is sent.

The agentic workflow is built using **LangGraph** with a shared state passed between agents.

## Current Architecture

```text
Patient Data
     |
     v
+-------------------+
|  Summary Agent    |
+-------------------+
     |
     v
+-------------------+
|  Reminder Agent   |
+-------------------+
     |
     v
+-------------------+
| Escalation Agent  |
+-------------------+
     |
     v
  Conditional Routing
     |
     +----------------------+
     |                      |
     v                      v
Escalation Review      Human Approval
     |                      |
     +----------+-----------+
                |
                v
               END
```

## Agents

### 1. Patient Summary Agent

Creates a structured summary of the patient's previous visit and follow-up requirements.

The summary currently includes:

- Diagnosis
- Previous visit outcome
- Medications
- Next steps
- Required tests
- Follow-up date
- Important concerns
- Case severity

### 2. Reminder Agent

Uses the patient summary to create a personalized follow-up reminder.

The reminder includes:

- Follow-up date
- Required tests
- Reason for required tests
- Next steps
- Case-specific concerns
- Priority

All generated reminders currently require **human approval** before they can be considered for sending.

### 3. Escalation Agent

Evaluates the patient's contact history and case severity to determine whether escalation is required.

Current business rules include:

| Case | Escalation condition |
|---|---|
| High severity | At least 1 no-response attempt |
| Medium severity | At least 2 no-response attempts |
| Normal severity | At least 2 no-response attempts |
| Patient responded | No escalation |

When escalation is required, the workflow identifies the recommended healthcare team members for review.

### 4. Human Approval

The system follows a **human-in-the-loop** approach.

The AI does not independently send patient communications.

A human reviewer can currently:

- Approve a reminder
- Reject a reminder

The approval step is implemented as part of the LangGraph workflow.

## Technology Stack

- **Python**
- **LangGraph** — agent workflow and state management
- **LangChain** — LLM/agent integration
- **AWS Bedrock** — planned LLM backend
- **Boto3** — AWS integration
- **ChromaDB** — planned vector database for RAG
- **Streamlit** — planned user interface
- **AWS EC2** — planned deployment
- **Amazon S3** — planned storage

## Project Structure

```text
careloop/
│
├── agentic_ai/
│   ├── __init__.py
│   ├── state.py
│   ├── summary_agent.py
│   ├── reminder_agent.py
│   ├── escalation_agent.py
│   ├── workflow.py
│   │
│   ├── test_state.py
│   ├── test_summary.py
│   ├── test_reminder.py
│   ├── test_escalation.py
│   └── test_llm.py
│
├── run_workflow.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone <REPOSITORY_URL>
cd ai-patient-follow-up-assistant
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Current Workflow

From the project root:

```bash
python run_workflow.py
```

The current prototype runs the following sequence:

```text
Summary
   ↓
Reminder
   ↓
Escalation
   ↓
Conditional Routing
   ↓
Escalation Review (when required)
   ↓
Human Approval
   ↓
END
```

The human approval step currently runs through the terminal.

Example:

```text
HUMAN APPROVAL REQUIRED

Reminder Subject:
Follow-up Reminder - 2026-10-15

Options:
  [a] Approve
  [r] Reject
```

## Current Implementation Status

### Completed

- [x] Shared typed patient state
- [x] Patient Summary Agent
- [x] Reminder Agent
- [x] Escalation Agent
- [x] LangGraph StateGraph
- [x] Sequential agent workflow
- [x] Conditional routing
- [x] Escalation review
- [x] Human-in-the-loop approval
- [x] Approve/reject flow
- [x] Synthetic patient test data
- [x] Basic agent unit tests
- [x] Local end-to-end workflow execution

### In Progress / Planned

- [ ] LLM integration through AWS Bedrock
- [ ] RAG pipeline
- [ ] Patient-context retrieval
- [ ] Tool-using agents
- [ ] Persistent memory/context handling
- [ ] Retry and error-handling mechanisms
- [ ] Input/output validation
- [ ] Human edit workflow
- [ ] Streamlit approval interface
- [ ] Additional workflow test scenarios
- [ ] AWS EC2 deployment
- [ ] S3 integration
- [ ] Final integration testing

## AWS / Bedrock

The project is designed to use **Amazon Bedrock** for LLM inference.

Configure AWS locally using:

```bash
aws configure
```

Verify the configured account:

```bash
aws sts get-caller-identity
```

Set the AWS region used by the project:

```text
us-east-1
```

### Important

Do **not** commit AWS credentials, API keys, `.env` files, or other secrets to GitHub.

The repository's `.gitignore` excludes:

```text
.env
.aws/
```

## Team Development

Each team member should:

1. Clone the repository.
2. Create their own Python virtual environment.
3. Install dependencies.
4. Configure their own AWS credentials.
5. Work on their assigned component.
6. Commit changes to their branch.
7. Push the branch to GitHub.
8. Create a Pull Request for integration.

Recommended branch naming:

```text
feature/summary-agent
feature/reminder-agent
feature/rag
feature/bedrock
feature/streamlit
feature/aws-deployment
```

## Design Principles

### Human-in-the-loop

AI recommendations are reviewed by a human before patient communication is sent.

### Stateful workflow

Agents communicate through a shared patient state rather than operating independently.

### Conditional routing

The workflow changes based on escalation requirements and patient contact history.

### Modular agents

Each agent has a specific responsibility so individual components can be tested and improved independently.

### Safety and validation

Patient-facing actions should be validated and reviewed rather than being executed blindly by the AI.

## Example Patient Flow

A patient has:

```text
Diagnosis:
Hypertension

Previous outcome:
Elevated blood pressure

Required tests:
- Blood pressure measurement
- Routine blood test

Follow-up:
2026-10-15

Severity:
Medium
```

The system:

1. Creates a structured patient summary.
2. Generates a personalized follow-up reminder.
3. Checks the patient's contact history.
4. Determines whether escalation is necessary.
5. Routes the case accordingly.
6. Requests human approval before the reminder proceeds.

## Disclaimer

This project is a **capstone prototype** intended for demonstration and educational purposes.

It is not a medical device and should not be used to make clinical decisions or independently communicate medical advice to patients.
