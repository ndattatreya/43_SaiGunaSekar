```md
# Medication Reminder Chatbot  
## Label-Aware & Risk-Adaptive AI System

---

## Overview

The **Medication Reminder Chatbot** is an AI-driven healthcare assistant that answers medicine-related questions and generates **personalized medication reminder plans** using **official FDA drug label data**.

Unlike conventional medication chatbots or reminder apps, this system **does not provide recommendations immediately**.  
Instead, it follows a **risk-adaptive, safety-first workflow**, similar to real clinical screening procedures.

The system is built using **Retrieval-Augmented Generation (RAG)** over regulatory drug data sourced from **openFDA**, ensuring responses are accurate, explainable, and compliant.

---

## Key Innovation: Risk-Adaptive Questioning

Traditional medication reminder applications rely on static reminders and generic warnings.

This project introduces a **label-aware, risk-driven interaction loop**, where the system dynamically adapts its behavior based on detected medical risks.

### What Makes This Project Novel

- Reads and interprets FDA drug label sections:
  - Warnings
  - Contraindications
  - Pregnancy risks
  - Drug interactions
- Automatically generates **mandatory safety questions**
- Requires structured user responses before proceeding
- Uses conditional reasoning to control outputs
- Prevents unsafe or premature recommendations

**No dosage or reminder plan is generated until all required safety questions are answered.**
---

## Example Interaction

### Step 1: User Query

```json
{
  "drug_name": "Isotretinoin",
  "intent": "dosage_and_reminder"
}
````

### Step 2: System-Generated Safety Questions

```json
{
  "questions": [
    "Are you currently pregnant or planning pregnancy?",
    "Do you consume alcohol regularly?",
    "Do you have any liver-related conditions?"
  ]
}
```

### Step 3: User Responses

```json
{
  "pregnant": "no",
  "alcohol_use": "yes",
  "liver_disease": "no"
}
```

### Step 4: Final Output (Conditionally Generated)

```json
{
  "drug": "Isotretinoin",
  "dosage_guidance": "Dosage must be strictly prescribed by a healthcare professional.",
  "personalized_warnings": [
    "Alcohol consumption increases the risk of liver damage."
  ],
  "reminder_plan": {
    "frequency": "once daily",
    "time": "after meals",
    "notes": [
      "Avoid alcohol",
      "Periodic liver function tests recommended"
    ]
  },
  "safety_notice": "Consult a healthcare professional before use."
}
```

---

## System Architecture

### 1. Drug Label Ingestion

* Downloads FDA drug label data from **openFDA**
* Parses critical sections:

  * Indications & Usage
  * Dosage & Administration
  * Warnings
  * Contraindications
  * Drug Interactions
* Converts text into embeddings
* Stores embeddings in **ChromaDB**

---

### 2. Retrieval-Augmented Generation (RAG)

* Uses **LangChain** for orchestration
* Retrieves only relevant FDA label passages
* Prevents hallucinated medical advice
* Ensures outputs are grounded in regulatory data

---

### 3. Risk Detection Engine

* Scans retrieved label content
* Detects high-risk indicators such as:

  * Pregnancy-related risks
  * Liver toxicity
  * Alcohol interactions
  * Drug–drug interactions
* Maps detected risks to **mandatory safety questions**

---

### 4. User Input Handling

* Stores responses in a session context
* Validates and normalizes inputs
* Drives conditional logic for downstream decisions

---

### 5. Conditional Recommendation Generator

* Combines rule-based logic with LLM reasoning
* Recommendations depend strictly on:

  * FDA label constraints
  * User-provided responses
* Automatically blocks unsafe outputs

#### Example Logic

```
IF pregnancy == yes
    → Block dosage recommendation
ELSE
    → Proceed

IF alcohol_use == yes
    → Add liver toxicity warning
```

---

## Tech Stack

| Layer                  | Technology                       |
| ---------------------- | -------------------------------- |
| Programming Language   | Python 3                         |
| LLM Orchestration      | LangChain                        |
| Vector Database        | ChromaDB                         |
| Embeddings             | Sentence Transformers / OpenAI   |
| Backend API (Optional) | FastAPI                          |
| Data Source            | FDA Drug Label Dataset (openFDA) |

---

## API Endpoints (Optional)

### Ask Drug Question

```
POST /ask_drug
```

### Submit Safety Answers

```
POST /submit_answers
```

### Generate Reminder Plan

```
POST /generate_reminder
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ndattatreya/43_SaiGunaSekar.git
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download FDA Drug Label Data

```bash
python scripts/download_fda_labels.py
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

---

## Safety & Ethics

* No diagnosis or treatment decisions are made
* Responses are strictly derived from FDA drug labels
* Explicit medical disclaimers are included
* Users are encouraged to consult healthcare professionals
* Designed to minimize hallucination and misuse

---

## Use Cases

* Medication reminder systems
* Healthcare AI research projects
* RAG-based medical assistants
* Regulatory-safe AI demonstrations
* Academic and capstone projects

---

## Disclaimer

This project is intended **for educational and research purposes only**.

It **does not replace professional medical advice, diagnosis, or treatment**.
Always consult a licensed healthcare professional before making medical decisions.

---

## Future Enhancements

* Multi-drug interaction reasoning
* Voice-based medication reminders
* Temporal dose conflict detection
* Patient profile memory (age, conditions)
* EHR integration (research use only)

---
