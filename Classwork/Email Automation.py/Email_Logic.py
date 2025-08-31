'''
 # Email Automation:

- when we send email to user weuse email automation to send emails automatically.
- To send bulk emails 
- The email and the password we created are the sender mail(the one who sends the emails)


1) smtp - simple mail transport protocol  ----for sending emails
2) os - for file path and file existence checks
3) csv file - To read email addresses from a CSV file.
4) MIMEMultipart - It allows to attach file and text. ----- for creating multipart email messages
5) MIMEText - Is for adding plain text to email body


'''

import smtplib   # Simple mail transport protocol for sending emails
import os        # For file path and file existence checks
import csv       # To read email addresses from a CSV file
from email.mime.multipart import MIMEMultipart   # For creating multipart email messages
from email.mime.text import MIMEText    # For adding plain text to email body

# https://myaccount.google.com/apppasswords

#we need to create some variabe 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587 # port used for TLS (encription)  
SENDER_EMAIL = " vaishnavi.thandus@gmail.com"
SENDER_PASSWORD = "rneb ivig mswn huzt"

'''
- receiver email can be with any domain (ex: Yahoo, gmail.com)
- sender gmail needs be gmail.com
- if we want to send it from other domain we need to have access to that domain mail
- to initialize the Layers we use port no's

'''
def send_email(to_email, subject, body):
    try:
        # Creating the msg body
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Starting the Server (sending msg through SMTP library)
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")

    except  Exception as e:
        print(f"Error sending email to {to_email}: {e}")

# For sending Bulk emails

def send_bulk_emails(csv_file, subject, body):
    try:
        csv_path = os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f"Error: CSV file '{csv_file}' not found.")
            return  # file exit
        
        '''
  We have 2 ways to open a file
 
 with open ------- as file:
newline - 
encoding - to convert from bytes to string,csv is stored in bytes.


 '''
        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)  
            for row in reader:
                if row:
                    email = row[0]
                    send_email(email, subject, body)

    except Exception as e:
        print(f"Error reading CSV file: {e}")

        