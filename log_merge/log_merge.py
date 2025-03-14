import os
from log_sorter.log_sorter import parse_timestamp
#Merges log files, sorts them by timestamp, and writes to an output file 
def merge_log_files(folder_path, log_files, output_file):
#List to store all log lines
    all_lines = []
 
    #Loop through each valid log file
    for log_file in log_files:
        file_path = os.path.join(folder_path, log_file)
 
        try:
            #Open the file and read all lines
            with open(file_path, "r") as f:
                lines = f.readlines()
                #Add the lines to the list
                all_lines.extend(lines)
 
        except Exception as e:
            #Print an error message if the file cannot be read
            print(f"Error reading {log_file}: {e}")
 
    #Sort all log lines based on timestamps
    all_lines.sort(key=parse_timestamp)
 
    #Write the sorted log lines into the output file
    with open(output_file, "w") as out:
        for line in all_lines:
            out.write(line)
