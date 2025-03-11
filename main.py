import os#os interact with system files,checks if a folder exists or list files

folder_path=input("Enter the folder path: ")#it prompts the user to enter the folder path

if not os.path.isdir(folder_path):#checks if the given folder path is a vaild directory or not
    print("The provided path is not valid, please provide a valid folder path ")
else:
    files=os.listdir(folder_path) #get the list of files in the folder

    if not files: #checks if the folder is empty 
        print("The provided folder is Empty")
    else:
        print("Processing")
        log_file_count=0
        Invalid_file_found=0

        for file in files:
            if file.endswith('.log'):
                log_file_count = log_file_count+1
            else:
                Invalid_file_found = Invalid_file_found+1
           
                
        if log_file_count>0:#checks for files
            print(f"Total Log files found: {log_file_count:}")
            print(f"Invalid files found: {Invalid_file_found:}")
        elif log_file_count == 0:
            print(f"Total Log files found: {log_file_count:}")
            print(f"Invalid files found: {Invalid_file_found:}")
            print("The provided folder doesn't have any log files, please provide a valid folder")
        
