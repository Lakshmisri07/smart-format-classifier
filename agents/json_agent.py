import json
import uuid
from datetime import datetime

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def validate_and_extract(self, json_content):
        # Expected schema keys — you can customize this
        expected_keys = ["invoice_id", "amount", "date", "customer"]

        missing_fields = [key for key in expected_keys if key not in json_content]

        # Extract only expected fields (use None if missing)
        extracted = {key: json_content.get(key) for key in expected_keys}

        return extracted, missing_fields

    def process(self, file_path):
        try:
            with open(file_path, 'r') as f:
                json_content = json.load(f)

            extracted, missing_fields = self.validate_and_extract(json_content)

            # Use shared memory to store thread_id & timestamp consistently
            thread_id = str(uuid.uuid4())
            timestamp = datetime.now().isoformat()

            status = "Success"
            if missing_fields:
                status = f"Missing fields: {missing_fields}"

            log_entry = {
                "agent": "JSONAgent",            # Added agent name for clarity
                "source": file_path,
                "type": "JSON",
                "timestamp": timestamp,
                "thread_id": thread_id,
                "extracted_values": extracted,
                "missing_fields": missing_fields,
                "status": status
            }

            self.memory.log(log_entry)
            print(f"[JSONAgent] Processed JSON '{file_path}' with status: {status}")

        except Exception as e:
            # Log failure with timestamp and thread_id
            log_entry = {
                "agent": "JSONAgent",
                "source": file_path,
                "type": "JSON",
                "timestamp": datetime.now().isoformat(),
                "thread_id": str(uuid.uuid4()),
                "status": f"Failed - {str(e)}"
            }
            self.memory.log(log_entry)
            print(f"[JSONAgent] Error processing JSON '{file_path}': {e}")
