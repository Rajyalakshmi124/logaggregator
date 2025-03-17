#os module provides a way to interact with the operating system, allowing you to perform tasks like accessing files and directories
import os 
from file_handler.file_handler import get_log_files, merge_log_files
from file_validation.file_validation import file_validation
from config import LOGS_FOLDER, OUTPUT_FOLDER

EMPTY_FOLDER = "The provided folder is Empty"
INVALID_FOLDER_PATH = "The provided path is not valid, please provide a valid folder path"
INVALID_FOLDER_COUNT="Invalid files found"
LOG_FILE_EXTENSION = ".log"
NO_LOG_FILES = "The provided folder doesn't have any log files, please provide a valid log folder"
PROCESSING = "Processing"
TOTAL_LOG_FILE_FOUND = "Total Log files found"

#main entry point of the script
if __name__ == "__main__":
    #prompt the user to enter the folder path   
    folder_path = input("Enter the folder path: ")
    
    #It returns an error message the list of log files, the count of log files, and the count of invalid files
    error_message, log_files, log_file_count, invalid_file_count = file_validation(folder_path)
    # If there's an error message, print it
    if error_message:
        print(error_message)
    # Otherwise, print the count of log files and invalid files
    else:
        print(f"Total Log files found: {log_file_count}")
        print(f"Invalid files found: {invalid_file_count}")

        # If log files exist, merge them
        if log_files:
            # os.makedirs(folder_path,exist_ok=True)
            output_file = os.path.join(folder_path, "merged_logs.txt")
            merge_log_files(folder_path, log_files, output_file)
            print(f"Merged log file created: {output_file}")
        else:
            print(f"{NO_LOG_FILES}")
