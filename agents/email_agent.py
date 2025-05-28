import re
import uuid
from datetime import datetime

INTENT_KEYWORDS = {
    "Invoice": ["invoice", "bill", "amount due"],
    "RFQ": ["request for quote", "rfq", "quotation"],
    "Complaint": ["complaint", "issue", "problem"],
    "Regulation": ["section", "clause", "regulation"],
}

URGENCY_KEYWORDS = {
    "High": ["urgent", "asap", "immediately", "important"],
    "Medium": ["soon", "priority"],
    "Low": ["whenever", "no rush", "later"]
}

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def extract_sender(self, email_text):
        # Simple regex to extract "From: someone@example.com"
        match = re.search(r"From:\s*(.+)", email_text)
        if match:
            return match.group(1).strip()
        return "Unknown"

    def detect_intent(self, text):
        text = text.lower()
        for intent, keywords in INTENT_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                return intent
        return "Other"

    def detect_urgency(self, text):
        text = text.lower()
        for level, keywords in URGENCY_KEYWORDS.items():
            if any(kw in text for kw in keywords):
                return level
        return "Normal"

    def process(self, email_text):
        sender = self.extract_sender(email_text)
        intent = self.detect_intent(email_text)
        urgency = self.detect_urgency(email_text)

        thread_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()

        extracted_values = {
            "sender": sender,
            "intent": intent,
            "urgency": urgency,
            # You can add more fields like subject, body preview, etc.
        }

        log_entry = {
            "agent": "EmailAgent",
            "source": sender,
            "type": "Email",
            "timestamp": timestamp,
            "thread_id": thread_id,
            "extracted_values": extracted_values,
            "status": "Success"
        }

        self.memory.log(log_entry)

        print(f"[EmailAgent] Processed Email from '{sender}' with intent '{intent}' and urgency '{urgency}'")
