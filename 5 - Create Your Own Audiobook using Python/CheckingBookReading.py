from gtts import gTTS
from PyPDF2 import PdfReader
import os

def read_pdf_with_gtts(pdf_file_path):
    # Open the PDF file in read-binary mode
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)

        # Get the number of pages in the PDF
        number_of_pages = len(reader.pages)
        print(f"Number of pages: {number_of_pages}")

        # Loop through all pages
        for i in range(number_of_pages):
            page = reader.pages[i]  # Access each page
            page_content = page.extract_text()  # Extract text from the page

            if page_content:  # Check if there is content on the page
                # Determine language based on content
                lang = 'hi' if any(char in page_content for char in 'अआइईउऊऍऎओऔ') else 'en'
                
                # Create a gTTS object
                tts = gTTS(text=page_content, lang=lang)
                
                # Save the audio to an MP3 file
                audio_file = f'page_{i + 1}_audio.mp3'
                tts.save(audio_file)

                # Optionally, play the audio file (uncomment the line below)
                os.system(f'start {audio_file}')  # For Windows; use 'open' for macOS or 'xdg-open' for Linux

# Replace with the path to your PDF file
pdf_file_path = r"E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\5 - Create Your Own Audiobook using Python\आपके अवचेतन मन की शक्ति.pdf"
read_pdf_with_gtts(pdf_file_path)
