import os
from datetime import datetime

# Extracts and parses the timestamp from a log line.
def parse_timestamp(line):
    formats = ["%Y/%m/%d %H:%M:%S:%f", "%Y-%m-%dT%H:%M:%S.%fZ", "%m/%d/%Y %H:%M:%S.%f"]
    for fmt in formats:
        try:
            timestamp_str = line.split()[0] + " " + line.split()[1]
            # Convert the extracted string timestamp to a datetime object
            return datetime.strptime(timestamp_str, fmt)
        except (IndexError, ValueError):
            continue
    return datetime.min

# Merges log files, sorts them by timestamp, and writes to an output file 
def merge_log_files(folder_path, log_files, output_file):
    # List to store all log lines
    all_lines = []

    # Loop through each valid log file
    for log_file in log_files:
        file_path = os.path.join(folder_path, log_file)

        try:
            # Open the file and read all lines
            #"r" specifies that the file should be opened in read mode
#           #"f" is used to perform operations on the file (like reading)
            with open(file_path, "r") as f:
                lines = f.readlines()
                # Add the lines to the list
                all_lines.extend(lines)
        #except handles the exception if it  occurs
        #e is an object of Exception
        except Exception as e:
            # Print an error message if the file cannot be read
            print(f"Error reading {log_file}: {e}")

    # Sort all log lines based on timestamps
    all_lines.sort(key=parse_timestamp)

    # Write the sorted log lines into the output file
    #"w" mode opens the file in writing only mode
    with open(output_file, "w") as out:
        for line in all_lines:
            out.write(line)
