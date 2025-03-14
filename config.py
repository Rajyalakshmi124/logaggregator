import os
 
# Define default directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))#represents the current file location
LOGS_FOLDER = os.path.join(BASE_DIR, "logs")        # Default log storage
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output") #this is the location where the merged log file will be saved
