import os#os interact with system files,checks if a folder exists or list files

folder_path=input("Enter the folder path: ")#it prompts the user to enter the folder path
print("Processing")

if not os.path.isdir(folder_path):#checks if the given folder path is a vaild directory or not
    print("The provided path is not valid, please provide a valid folder path ")
else:
    files=os.listdir(folder_path) #get the list of files in the folder
    if not files: #checks if the folder is empty 
        print("The provided folder is Empty")
    else:
        log_file_count=0
        txt_file_count=0#counts the number of .log files in the folder
        png_file_count=0
        other_file_count=0

        for file in files:
            if file.endswith('.log'):
                log_file_count = log_file_count+1
            elif file.endswith('.txt'):
                txt_file_count = txt_file_count+1
            elif file.endswith('.png'):
                png_file_count = png_file_count+1
            else:
                other_file_count = other_file_count+1
                
        if log_file_count>0:
            print(f"Total Log files found: {log_file_count:}")
            print(f"Total txt_file found: {txt_file_count:}")
            print(f"Total png_file found: {png_file_count:}")
            print(f"Total other_file found: {other_file_count:}")
        
    
