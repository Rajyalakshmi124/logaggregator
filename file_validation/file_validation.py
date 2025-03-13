import os
#Importing constants
from constants.constants import *
#Checks if the folder is valid and retrieves the file list
def file_validation(folder_path):
    #Check if the provided folder path is valid or not
    if not os.path.isdir(folder_path):
        #Return an error message, an empty list, and 0 counts
        return INVALID_FOLDER_PATH, [], 0, 0
    #Retrieve the list of files in the folder
    files = os.listdir(folder_path)
    #If the folder is empty, return an appropriate message and empty data
    if not files:
        return EMPTY_FOLDER, [], 0, 0
    print(PROCESSING)
    # Filter out only `.log` files from the list of files
    log_files = [file for file in files if file.endswith(".log")]
     # Count the number of `.log` files
    log_file_count = len(log_files)
     # Count the number of invalid files (total files - log files)
    invalid_file_count = len(files) - log_file_count
    #Return None,the list of log files, the log file count, and the invalid file count
    return None, log_files, log_file_count, invalid_file_count