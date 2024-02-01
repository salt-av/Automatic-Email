import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import ssl
from email.message import EmailMessage

em = EmailMessage()

subject = ""
body = ""  
to_email = ""
smtp_server = "smtp.gmail.com"
smtp_port = 465
smtp_username = "vtsl5819@gmail.com"
smtp_password = "vklvjwsjcilcbyqm"

em['From'] = smtp_username
em['To'] = to_email
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(smtp_username, smtp_password)
    for i in range(500):
        smtp.sendmail(smtp_username, to_email, em.as_string())