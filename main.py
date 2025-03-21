import os
from log_merge.log_merge import merge_log_files
from file_validation.file_validation import file_validation
from database.audit import log_audit_entry

# Main function to handle log file validation and merging
def main():
    # User input for target logs folder path
    folder_path = input("Enter the folder path: ")
 
    # Calling 'file_validation' function to validate 
    error_message, log_files, log_file_count, invalid_file_count = file_validation(folder_path)
 
    if error_message:
        log_audit_entry(folder_path, log_files, None, error_message)
        print(error_message)
    else:
        #Print the total number of log files found and invalid files count
        print(f"Total Log files found: {log_file_count}")
        print(f"Invalid files found: {invalid_file_count}")
 
        #If valid log files are present, proceed with merging
        if log_files:
            output_folder = input("Please specify the folder where you want to store the output merged file: ")
            output_file = os.path.join(output_folder, "merged_logs.txt")
 
            #Trying to merge log files and handle any permission errors
            try:
                #Calling 'merge_log_files' function to merge logs and save the output
                merge_log_files(folder_path, log_files, output_file)
                print(f"Merged log file created: {output_file}")
                log_audit_entry(folder_path, log_files, output_file)

            except Exception as e:
                log_audit_entry(folder_path, log_files, None, error_message)
        else:
            log_audit_entry(folder_path, log_files, None, "The provided folder doesn't have any log files, please provide a valid log folder")
            print("The provided folder doesn't have any log files, please provide a valid log folder")
 
# Entry point for the script, ensures 'main()' function runs when script is executed directly
if __name__ == "__main__":
    main()
