#importing the file_validation function from the file_validation module
from file_validation.file_validation import file_validation
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
        