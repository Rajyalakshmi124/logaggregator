#Datetime module that permits for the control of datetime objects
from datetime import datetime
#Extracts and parses the timestamp from a log line.
def parse_timestamp(line):

    try:
        #extract the timestamp by splitting the line and removing brackets
        timestamp_str = line.split()[0]
 
        #Convert the extracted string timestamp to a datetime object
        return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
 
    except (IndexError, ValueError):
        #If parsing fails, return the earliest possible datetime
        return datetime.min
