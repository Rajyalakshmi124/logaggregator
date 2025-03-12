#os module to interact with system files,checks if a folder exists or list files
import os
from constants import *

#it prompts the user to enter the folder path
folder_path=input("Enter the folder path: ")
#checks if the given folder path is a vaild directory or not
if not os.path.isdir(folder_path):
    print(f"{INVALID_FOLDER_PATH}") 
else:
    # if file exists this retrieves a list of files in the folder
    files=os.listdir(folder_path)

    #checks if the folder is empty 
    if not files: 
        print(f"{EMPTY_FOLDER}")
    else:
        print(f"{PROCESSING}")
        #count .log files, ensure a proper count of .log files in the given folder
        log_file_count=0
        #initialize counter for non-log files, count non-log files
        invalid_file_found=0
        #loop through each file in the folder
        for file in files:
            if file.endswith('.log'):#checks if the file has a .log extension 
                
                log_file_count = log_file_count+1 # increment log file count
            else:
                invalid_file_found = invalid_file_found+1 #increment invalid file count
        if log_file_count>0:#check if there are any log files
            print(f"TOTAL_LOG_FILE_FOUND: {log_file_count:}")
            print(f"INVALID_FOLDER_COUNT: {invalid_file_found:}")
        else:
            print(f"TOTAL_LOG_FILE_FOUND: {log_file_count}")
            print(f"INVALID_FOLDER_COUNT: {invalid_file_found}")
            print(f"{NO_LOG_FILES}")
        