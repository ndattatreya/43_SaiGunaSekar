RISK_PATTERNS = {
    "pregnancy": {
        "keywords": ["pregnancy", "pregnant", "fetal", "teratogenic"],
        "question": "Are you currently pregnant or planning pregnancy?",
        "blocks_dosage": True
    },
    "alcohol": {
        "keywords": ["alcohol", "ethanol"],
        "question": "Do you consume alcohol regularly?",
        "blocks_dosage": False
    },
    "liver": {
        "keywords": ["liver", "hepatic", "hepatotoxic"],
        "question": "Do you have any liver-related conditions?",
        "blocks_dosage": False
    },
    "kidney": {
        "keywords": ["kidney", "renal"],
        "question": "Do you have any kidney-related conditions?",
        "blocks_dosage": False
    }
}

def detect_risks(label_text):
    label_text = label_text.lower()
    detected = []

    for risk, cfg in RISK_PATTERNS.items():
        if any(k in label_text for k in cfg["keywords"]):
            detected.append({
                "risk": risk,
                "question": cfg["question"],
                "blocks_dosage": cfg["blocks_dosage"]
            })

    return detected

def evaluate_answers(detected_risks, user_answers):
    dosage_allowed = True
    warnings = []

    for r in detected_risks:
        answer = user_answers.get(r["risk"], "").lower()

        if answer == "yes" and r["blocks_dosage"]:
            dosage_allowed = False
            warnings.append(f"Medication contraindicated due to {r['risk']} risk.")
        elif answer == "yes":
            warnings.append(f"Use caution due to {r['risk']} risk.")

    return dosage_allowed, warnings