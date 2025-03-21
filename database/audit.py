from datetime import datetime
from database.db_connection import get_db

def log_audit_entry(folder_path, log_files, output_file, error_message=None):
    db = get_db()
    audit_collection = db["audit"]  # collection name
    # Create the audit entry
    audit_entry = {
        "folder_path": folder_path,
        "file_count": len(log_files),
        "file_names": log_files,
        "operation_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": "Error" if error_message else "Success",
        "output_file": output_file if not error_message else None,
        "error_message": error_message or ""
    }
    # Insert the audit entry into the collection
    audit_collection.insert_one(audit_entry)
