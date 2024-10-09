import os
from datetime import datetime



# Replace this with the full path to your file
file_path = r'E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\10 - Extract File Matadata with Python\OfferLetter.py'

# Check if the file exists
if os.path.isfile(file_path):
    FileStatistics = os.stat(file_path)
    print(FileStatistics)
else:
    print(f"The file '{file_path}' does not exist.")

""" Output - It is getting file Statistics successfully
os.stat_result(st_mode=33206, st_ino=844424930149315, st_dev=346201721, st_nlink=1, st_uid=0, st_gid=0, st_size=1283, st_atime=1728411520, st_mtime=1728411520, st_ctime=1728411519)
"""

##FileStatistics = os.stat('Find Highest Integer in List.py')
##print(FileStatistics)
