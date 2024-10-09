import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up your email and app password
email = "backuplappy880@gmail.com"  # Replace with your email
app_password = "ayhv rbtd nknu szsh"  # Replace with your app password

# Create the email
subject = "Automation Anywhere Offer Letter"
body = """Dear Shubam Mahajan
We are very pleased to inform you  that you've been shortlisted and going to be a part of
Automation Anywhere. You have option to choose the location from either Bangalore or vadodara.
We're looking forward to hear from you..."""

msg = MIMEMultipart()
msg['From'] = 'mhajan.shubh@gmail.com'
msg['To'] = 'shubhammahajan400@gmail.com'  # Sending to yourself
msg['Subject'] = 'Automation Anywhere Offer Letter'
contents=["<h2> Find the letter</h2>", "<p>All details here..!</p>"],
attachments=[r"E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\3 - Email Automation using Python\OfferLetter_ShubhamMahajan.pdf",r"E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\3 - Email Automation using Python\Automaiton Anywhere.png"]

# Attach the body to the email
msg.attach(MIMEText(body, 'plain'))

# Send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade to secure connection
        server.login(email, app_password)  # Login to your email account
        server.send_message(msg)  # Send the email
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")
