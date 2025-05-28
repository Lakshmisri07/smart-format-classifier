from PyPDF2 import PdfReader
from datetime import datetime

class PDFAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, file_path):
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            intent = "Invoice" if "invoice" in text.lower() else "Regulation" if "section" in text.lower() else "Other"

            log_entry = {
                "agent": "PDFAgent",
                "intent": intent,
                "preview": text[:200] + "...",
                "status": "Success",
                "source": file_path,
                "timestamp": datetime.now().isoformat()
            }

            self.memory.log(log_entry)
            print(f"[PDFAgent] ✅ PDF processed. Intent: {intent}")

        except Exception as e:
            self.memory.log({
                "agent": "PDFAgent",
                "source": file_path,
                "status": f"Failed - {str(e)}",
                "timestamp": datetime.now().isoformat()
            })
            print(f"[PDFAgent] ❌ Error: {e}")
