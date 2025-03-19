import os
from file_handler.file_handler import get_log_files, merge_log_files
from file_validation.file_validation import file_validation
from config import LOGS_FOLDER, OUTPUT_FOLDER
 
# Main function to handle log file validation and merging
def main():
    # Asking the user to input the folder path where logs are present
    folder_path = input("Enter the folder path: ")
 
    # Calling 'file_validation' function to validate the folder and get the list of log files
    error_message, log_files, log_file_count, invalid_file_count = file_validation(folder_path)
 
    # If there's an error message, print it (like invalid path or empty folder)
    if error_message:
        print(error_message)
    else:
        # Print the total number of log files found and invalid files count
        print(f"Total Log files found: {log_file_count}")
        print(f"Invalid files found: {invalid_file_count}")
 
        # If valid log files are present, proceed with merging
        if log_files:
            # Asking the user to provide the folder to save the merged log file
            output_folder = input("Please specify the folder where you want to store the output merged file: ")
 
            # Creating the output file path for merged logs
            output_file = os.path.join(output_folder, "merged_logs.txt")
 
            # Trying to merge log files and handle any permission errors
            try:
                # Calling 'merge_log_files' function to merge logs and save the output
                merge_log_files(folder_path, log_files, output_file)
                print(f"Merged log file created: {output_file}")
 
            # Handling 'PermissionError' in case the user doesn't have write access to the folder
            except PermissionError:
                print(f"Permission denied: '{output_file}'. Please choose a different folder.")
 
                # Asking the user to provide a different folder for storing the merged file
                output_folder = input("Please specify a different folder where you want to store the output merged file: ")
                output_file = os.path.join(output_folder, "merged_logs.txt")
 
                # Merging logs again in the new folder
                merge_log_files(folder_path, log_files, output_file)
                print(f"Merged log file created: {output_file}")
 
        # If no log files are found, print the appropriate message
        else:
            print("The provided folder doesn't have any log files, please provide a valid log folder")
 
# Entry point for the script, ensures 'main()' function runs when script is executed directly
if __name__ == "__main__":
    main()
