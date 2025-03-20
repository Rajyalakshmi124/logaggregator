import os
FILE_EXTENSION = ".log"

#Checks if the folder is valid and retrieves the file list
def file_validation(folder_path):
    if not os.path.isdir(folder_path):
        return "The provided path is not valid, please provide a valid folder path", [], 0, 0
    #Retrieve the list of files in the folder
    files = os.listdir(folder_path)
    if not files:
        return "The provided folder is Empty", [], 0, 0
    print("Processing")
    # Filter out only `.log` files from the list of files
    log_files = [file for file in files if file.endswith(f"{FILE_EXTENSION}")]
    log_file_count = len(log_files)
    invalid_file_count = len(files) - log_file_count
    return None, log_files, log_file_count, invalid_file_count
