from memory.shared_memory import SharedMemory
from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from agents.pdf_agent import PDFAgent

def main():
    memory = SharedMemory()
    classifier = ClassifierAgent()

    filepath = input("Enter the path of your file (PDF/JSON/Email): ")
    fmt, intent, content = classifier.classify(filepath)

    print(f"\n[Classifier] Format: {fmt}, Intent: {intent}")
    print(f"[Classifier] Routing to appropriate agent...")

    if fmt == "JSON":
        agent = JSONAgent(memory)
        agent.process(filepath)
    elif fmt == "Email":
        agent = EmailAgent(memory)
        agent.process(content)
    elif fmt == "PDF":
        agent = PDFAgent(memory)
        agent.process(filepath)

if __name__ == "__main__":
    main()
