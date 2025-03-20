from datetime import datetime

#Extracts and parses the timestamp from a log line.
def parse_timestamp(line):
    try:
        timestamp_str = line.split()[0]
        #Convert the extracted string timestamp to a datetime object
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
 
    except (IndexError, ValueError):
        return datetime.min
