import webbrowser

with open(r"E:\\DarkBox\\12 LPA - Shubham Mahajan_Automtion Anywhere\\Finally Bro...!!\\Python_Automation_Projects\\8 - Automate Bookmarked Websited using Python\\List of websites I visit regularly.txt") as file:
    links = file.readlines()
    
    # Open each link in the default web browser
    for link in links:
        webbrowser.get('windows-default').open(link.strip())  # Use strip() to remove any newline characters
