import pyttsx3

"""
engine = pyttsx3.init()

#Checking for a written text first, it is working or not
text = "Shubam Mahajan got placed in Automation Anywhere at the package of 12 LPA"
engine.say(text)

engine.runAndWait() # it's woking Perfectly
"""


import pyttsx3
from PyPDF2 import PdfReader

# Open the PDF file in read-binary mode
pdf_file_path = r"E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\5 - Create Your Own Audiobook using Python\OfferLetter_ShubhamMahajan.pdf"
with open(pdf_file_path, 'rb') as file:
    # Create a PdfReader object
    reader = PdfReader(file)

    # Get the number of pages in the PDF
    number_of_pages = len(reader.pages)
    print(f"Number of pages: {number_of_pages}")

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    for i in range(number_of_pages):  # Loop through all pages
        page = reader.pages[i]  # Access each page
        page_content = page.extract_text()  # Extract text from the page

        if page_content:  # Check if there is content on the page
            new_rate = 200  # Set the speech rate
            engine.setProperty('rate', new_rate)
            new_volume = 1.0  # Set the volume (0.0 to 1.0)
            engine.setProperty('volume', new_volume)

            # Get available voices and set one (index may vary)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)  # Change index if needed

            # Speak the content
            engine.say(page_content)

            # Save to an audio file (optional)
            engine.save_to_file(page_content, f'page_{i + 1}_audio.mp3')

            # Wait for the speech to finish
            engine.runAndWait()

# Stop the engine after processing
engine.stop()
