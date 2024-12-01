![Static Badge](https://img.shields.io/badge/pypi-v.2.2.0-blue?style=for-the-badge) 
![Static Badge](https://img.shields.io/badge/smtplib-v.3.12.4-green?style=for-the-badge&link=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsmtplib.html)
![Static Badge](https://img.shields.io/badge/email-v.4.0.2-brown?style=for-the-badge&link=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.html)


# Email Sender Verifier
![logo](images/logo.jpg)

Email Sender  Verifier is a python library designed for sending One-Time-Password (OTP) and performing code verification via email. This library is ideal for web applications that require a secure and straightforward method to authenticate users through email-based account verification ans OTPs.

## Installation
> Install Email Sender Verifier using pip.

CLI:

```bash
   pip install email-sender-verifier
```

```bash
   pip install https://github.com/christiangarcia0311/email-sender-verifier/raw/main/dist/email_sender_verifier-2.2.0.tar.gz
```

## Features

- Email Sending: Send emails with customizable subject, body and recipient.
- Easy Integration: Suitable for integration into web applications requiring email-based OTP and code verification.

## API

We added a simple email sender API using flask. The API allows other application to send email to users by making HTTP requests. It is designed to be easily integrated with other programming language/application or any other platform that can send HTTP requests.


EmailSender API: [Click here!](http://emailsender000.pythonanywhere.com/)

API Test Example sending HTTP request: [API Sample](https://github.com/christiangarcia0311/email-sender-verifier/raw/main/APITest/EmailSender_API.js)

> if you have an issue while opening the link please [contact me.](mailto:emailsender880@gmail.com)


## Usage

> Email Sender class import:

```python
    
    # import email sender class
    from Verifier.email import EmailSender
    
    # create new email sender object
    emailsender = EmailSender()

```

> Email Sender method:

```python

    """
    email_reciever (str): Specifies the recipient's email address where the email will be sent.
    msg_subject (str): Sets the subject line of the email.
    msg_body (str): Contains the main content of the email message.
    sender_name (str): holds the name of the sender.
    
    """
    
    # email sender method
    emailsender.send_email(email_reciever, msg_subject, msg_body, sender_name)

```


> Example 1 (Sending sample message):

```python
    
    # define the email details 
    email = 'username@gmail.com'
    subject = 'Sending email message using python.'
    body = 'This is example message from the author'
    name = 'EmailSender'
    
    # email sender method
    emailsender.send_email(email, subject, body, name)

```

> Example 2 (Using pyotp library):

```python
    
    # Secret key for pyotp
    secret_key = pyotp.random_base32()
    
    # Generate One-Time-Password using pyotp library
    totp = pyotp.TOTP(secret_key, interval=60)
    
    # define the email details
    email = 'username@gmail.com'
    subject = 'One-Time-Password using pyotp library'
    body = f'Your OTP code is: {totp.now()}'
    name = 'EmailSender'
    #email sender method
    emailsender.send_email(email, subject, body, name)

```

> Example 3 default sending:

```python
    email_reciever = 'reciever@gmail.com'
    
    #email sender method
    emailsender.send_email(email)
```


## LICENSE

![Static Badge](https://img.shields.io/badge/MIT-License-blue?style=for-the-badge&link=https%3A%2F%2Fraw.githubusercontent.com%2Fchristiangarcia0311%2Femail-sender-verification%2Fmain%2FLICENSE)

## Author

<img alt="Static Badge" src="https://img.shields.io/badge/Christian-Garcia-orange?style=for-the-badge&logo=github">

## Contact

For issues or feature requests, please open an issue on GitHub. Contributions, feature requests, and feedback are all welcome!




