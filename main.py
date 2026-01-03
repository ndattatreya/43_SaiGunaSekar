from data_ingestion import process_labels
from embedding_store import build_vector_store
from chatbot import interactive_medication_chatbot

def main():
    process_labels()
    collection, model = build_vector_store()
    interactive_medication_chatbot(collection, model)

if __name__ == "__main__":
    main()