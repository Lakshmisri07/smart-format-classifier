import json
import uuid
import time
from datetime import datetime
import os

class SharedMemory:
    def __init__(self, log_file='data/outputs/logs.json'):
        self.log_file = log_file
        # Ensure directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # Load existing logs from file or initialize empty list
        try:
            with open(self.log_file, 'r') as f:
                self.memory = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.memory = []

    def log(self, log_entry):
        # Add timestamp if not present
        if "timestamp" not in log_entry:
            # Use datetime for consistent format
            log_entry["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Add thread_id if not present
        if "thread_id" not in log_entry:
            log_entry["thread_id"] = str(uuid.uuid4())

        # Append to in-memory list
        self.memory.append(log_entry)

        # Save to file
        with open(self.log_file, 'w') as f:
            json.dump(self.memory, f, indent=4)

    def get_logs(self):
        return self.memory

    def generate_thread_id(self):
        return str(uuid.uuid4())
