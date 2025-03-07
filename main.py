import os#os interact with system files,checks if a folder exists or list files
folder_path=input("Enter the folder path: ")#it promots to user to enter the folder path
if os.path.isdir(folder_path):#checks if the given folder path is a vaild directory or not
    files=os.listdir(folder_path) #returns the list of files
    if files:
        print("Files Exists")
        log_file_found=False
        for file in files:#
            if file.endswith('.log'):#checks if the file has a .log extension 
                log_file_found=True
                if log_file_found:
                    print("Log files found")
                    continue#continue to the next iteration
                else:
                    print("No log file found")
            else:
                print("Not a log file")
        print("Processing")
    else:
        print("Invalid path")
                

                
        












    
    

    
