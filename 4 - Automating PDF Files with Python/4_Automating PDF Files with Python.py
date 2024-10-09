from PyPDF2 import PdfReader
from fpdf import FPDF

# Open the PDF file in read-binary mode
with open('OfferLetter_ShubhamMahajan.pdf', 'rb') as file:
    # Create a PdfReader object
    reader = PdfReader(file)
    
    # Print the number of pages
    print(len(reader.pages))#2
    
    # Optionally, print text from each page
    """
        for i, page in enumerate(reader.pages):
        text = page.extract_text()
        print(f"Page {i + 1} text: {text}")
    """

 # Access the third page (index 2)
    active_page = reader.pages[1]  # Remember that indexing starts at 0 so which page you want to print substrtact 1
    
    # Extract text from the active page
    text = active_page.extract_text()
    
    # Print the extracted text
    print(text)
    
""" Description as per page number(index)
Software Developer & Python Developer  
Automation Anywhere  
Phone: 9669999880  
Email: mhajan.shubh@gmail.com  
Acceptance of Offer:  
I, Shubham Mahajan , accept the terms of employment as outlined above.  
Date:  30/10/2024                                                                                                          Signature:   
"""

#Creating a new pdf using python and customize it.
##pdf = FPDF()
##pdf.add_page()
##pdf.set_font('helvetica',size = 12)
##pdf.cell(200,20, txt = "Quick tour to Automation Anywhere", ln = 1, align = "C")
##pdf.cell(txt = "THis is about your beginning of Corporate word, Be humble kepp  growing")
##pdf.output("Welcome to Automation Anywhere.pdf")

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size=12)

# Add a centered title
pdf.cell(200, 20, txt="Quick Tour to Automation Anywhere", ln=1, align="C")

# Add a second line of text
pdf.cell(0, 10, txt="This is about your beginning in the corporate world. Be humble and keep growing.", ln=1)

# Output the PDF
pdf.output("Welcome_to_Automation_Anywhere.pdf")






















