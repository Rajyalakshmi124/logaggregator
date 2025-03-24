from datetime import datetime
from database.db_connection import get_db

# Define constants for database and collection names
DATABASE_NAME = "logaggregator"
COLLECTION_NAME = "audit"

def log_audit_entry(folder_path, log_files, output_file, error_message=None):
    db = get_db()
    audit_collection = db[COLLECTION_NAME]
    
    # Create the audit entry
    audit_entry = {
        "folder_path": folder_path,
        "file_count": len(log_files),
        "file_names": log_files,
        "operation_time": datetime.now().isoformat(),
        "result": "Error" if error_message else "Success",
        "output_file": output_file if not error_message else None,
        "error_message": error_message or ""
    }
    
    #Check if the entry already exists
    existing_entry = audit_collection.find_one({
        "folder_path": folder_path,
        "operation_time": audit_entry["operation_time"]
    })
    
    if existing_entry:
        #Handle the case where the entry already exists
        print("An entry with the same folder path and operation time already exists.")
    else:
        #Insert the audit entry into the collection
        audit_collection.insert_one(audit_entry)
        print("Audit entry inserted successfully")
