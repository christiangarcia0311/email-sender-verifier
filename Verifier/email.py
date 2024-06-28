# Email Sender for Verification
# Python Email Sender Verification 
# Author: Christian Garcia


# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# _____RUNNABLE
# Sender class
class EmailSender:
  
  def __init__(self):
    
    # Server and port
    self.smtp_server = 'smtp.gmail.com'
    self.smtp_port = 587
    
    # Email configuration
    self.default_app_email = 'default03112003@gmail.com'
    self.default_app_pswd = 'kpkf nqkh rcbj hwqm'
    
  def send_email(self, email_reciever, msg_subject, msg_body, sender_name):
    
    # Create email message
    message = MIMEMultipart()
    message['From'] = f'{sender_name} <{self.default_app_email}>'
    message['To'] = email_reciever
    message['Subject'] = msg_subject
    message.attach(MIMEText(msg_body, 'plain'))
    
    # Send email by establishing connection
    try:
      server = smtplib.SMTP(self.smtp_server, self.smtp_port)
      server.starttls()
      server.login(self.default_app_email,
      self.default_app_pswd)
      server.sendmail(self.default_app_email, email_reciever, message.as_string())
      print('Email send successfully!')
    except Exception as e:
      print(f'Failed to send email: {e}')
    finally:
      server.quit()
