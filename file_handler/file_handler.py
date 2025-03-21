import os
from log_merge.log_merge import merge_log_files

FILE_EXTENSION = ".log"

#Fetches all log files from the given folder.
def get_log_files(folder_path):
 
    #List all files in the specified folder
    files = os.listdir(folder_path)
 
    #If no files are found, print a message and return an empty list
    if not files:
        print("The provided folder is Empty")
        return [], 0
 
    #Lists to store valid log files
    log_files = []
 
    #Counter for invalid files
    invalid_file_count = 0
 
    #Loop through all files in the folder
    for file in files:
        #Check if the file has the correct log file extension
        if file.endswith(FILE_EXTENSION):
            log_files.append(file)
 
    return log_files, invalid_file_count
