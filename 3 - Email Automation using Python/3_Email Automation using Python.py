import yagmail

# Set up your email and app password
email = "210305124088@paruluniversity.ac.in"
app_password = "jgbd mfcs puit rybl"  # Replace with your app password

# Create the yagmail SMTP client
yag = yagmail.SMTP(email, app_password)

try:
    # Send the email
    yag.send(
        to="210305124088@paruluniversity.ac.in",  # Recipient email
        cc="shubhammahajan400@gmail.com",          # CC email
        bcc="mahajanvitthal124@gmail.com",         # BCC email
        subject="Automation Anywhere Offer Letter",
        contents=["<h2> Find the letter</h2>", "<p>All details here..!</p>"],
        attachments=[
            r"E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\3 - Email Automation using Python\OfferLetter_ShubhamMahajan.pdf",
            r"E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\3 - Email Automation using Python\Automaiton Anywhere.png"
        ]
    )
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")
