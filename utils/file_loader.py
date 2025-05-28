# utils/file_loader.py

def load_file_content(filepath, format_type):
    content = ""
    if format_type == "JSON":
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    elif format_type == "Email":
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    elif format_type == "PDF":
        # Placeholder: for now, just return a message
        content = "PDF content extraction not implemented yet."
    else:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    return content
