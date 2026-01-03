from rag_query import ask_drug
from risk_engine import detect_risks, evaluate_answers

def interactive_medication_chatbot(collection, model):
    print("\n--- Medication Reminder Chatbot ---\n")

    drug = input("Enter the drug name: ").strip().lower()
    question = input("What is your question? ").strip()

    label_text = ask_drug(collection, model, drug, question)

    print("\nRelevant label info:\n")
    print(label_text[:700], "\n")

    detected_risks = detect_risks(label_text)
    user_answers = {}

    if detected_risks:
        print("Safety questions:\n")
        for r in detected_risks:
            ans = input(f"{r['question']} (yes/no): ")
            user_answers[r["risk"]] = ans

    allowed, warnings = evaluate_answers(detected_risks, user_answers)

    print("\n--- Recommendation ---\n")

    if not allowed:
        print("Dosage cannot be recommended.")
        for w in warnings:
            print("-", w)
        return

    print("Dosage allowed with caution.")
    for w in warnings:
        print("-", w)

    print("\nReminder: Once daily (sample plan)")