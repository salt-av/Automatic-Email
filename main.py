import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import ssl
from email.message import EmailMessage
import read
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

em = EmailMessage()

subject = "Invitation for **EVENT** " 
smtp_server = "smtp.gmail.com"
smtp_port = 465

smtp_username = os.environ.get('smtp_username', None)
smtp_password = os.environ.get('smtp_password', None)
em['From'] = smtp_username
em['Subject'] = subject

context = ssl.create_default_context()

rcvr_email, org_name = read.read_data()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(smtp_username, smtp_password)
    for email in rcvr_email:
        to_email = email
        em['To'] = to_email
        body = f"{org_name} is coordially invited to attend our Event."
        em.set_content(body)
        smtp.sendmail(smtp_username, to_email, em.as_string())
        
