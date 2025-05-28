import os
import json
from PyPDF2 import PdfReader

# Intent keywords and detection function (your existing code)
INTENT_KEYWORDS = {
    "Invoice": ["invoice", "bill", "amount due"],
    "RFQ": ["request for quote", "rfq", "quotation"],
    "Complaint": ["complaint", "issue", "problem"],
    "Regulation": ["section", "clause", "regulation"]
}

def detect_intent(text):
    text = text.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return intent
    return "Other"

class ClassifierAgent:
    def __init__(self):
        pass

    def detect_format(self, filepath):
        _, ext = os.path.splitext(filepath)
        ext = ext.lower()
        if ext == ".pdf":
            return "PDF"
        elif ext == ".json":
            return "JSON"
        elif ext == ".txt" or ext == ".eml":
            return "Email"
        else:
            return "Unknown"

    def extract_text(self, filepath):
        fmt = self.detect_format(filepath)
        if fmt == "PDF":
            try:
                reader = PdfReader(filepath)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
                return text
            except Exception as e:
                print(f"[ClassifierAgent] Error reading PDF: {e}")
                return ""
        elif fmt == "JSON":
            with open(filepath, 'r') as f:
                data = json.load(f)
            return json.dumps(data).lower()
        elif fmt == "Email":
            with open(filepath, 'r') as f:
                return f.read()
        else:
            return ""

    def classify(self, filepath):
        fmt = self.detect_format(filepath)
        content = self.extract_text(filepath)
        intent = detect_intent(content)
        return fmt, intent, content
