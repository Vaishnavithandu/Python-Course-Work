# Sending Single Email Logic: 

import Email_Logic

rec_mail = input("Enter the email: ")
subject = input("Enter the subject: ")
body = input("Enter the body: ")

Email_Logic.send_email(rec_mail, subject, body)
