import subprocess

FolderPath = r"D:\Placed,Congratulations\30LPA\It's time to\Companies"

try:
    subprocess.run(['explorer',FolderPath], check = False)
except subprocess.CalledProcessError:
    pass
