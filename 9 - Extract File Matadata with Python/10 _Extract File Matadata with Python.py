import os
from datetime import datetime

def GetFileMetadata(FilePath):
    # Check if the file exists
    if os.path.isfile(FilePath):
        FileStatistics = os.stat(FilePath)
        FileSize = FileStatistics.st_size
        LastModifiedDateTime = datetime.fromtimestamp(FileStatistics.st_mtime)

        print(f'The file size is: {FileSize} bytes')
        print(f'The latest modified date and time was: {LastModifiedDateTime}')  # Corrected variable name
    else:
        print(f"The file '{FilePath}' does not exist.")

# Use the correct file name with the full path
GetFileMetadata(r'E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\10 - Extract File Matadata with Python\OfferLetter.py')

""" Output for file - 
The file size is: 1283 bytes
The latest modified date and time was: 2024-10-08 23:48:40.232480
"""
