![Static Badge](https://img.shields.io/badge/pypi-v.2.3.1-blue)
![Static Badge](https://img.shields.io/badge/smtplib-v.3.12.4-green?link=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsmtplib.html)
![Static Badge](https://img.shields.io/badge/email-v.4.0.2-brown?link=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Femail.html)


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
   pip install https://github.com/christiangarcia0311/email-sender-verifier/raw/main/dist/email_sender_verifier-2.3.1.tar.gz
```

## Features

- Email Sending: Send emails with customizable subject, body and recipient.
- Easy Integration: Suitable for integration into web applications requiring email-based OTP and code verification.

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
    name = 'Administrator'
    
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
    name = 'Admin'
    #email sender method
    emailsender.send_email(email, subject, body, name)

```

> Example 3 (web-based otp verification using email sender):

![web-based](images/web-based.png)

- https://defaultapp11.pythonanywhere.com/

## LICENSE

![Static Badge](https://img.shields.io/badge/MIT-License-blue?link=https%3A%2F%2Fraw.githubusercontent.com%2Fchristiangarcia0311%2Femail-sender-verification%2Fmain%2FLICENSE)

## Author

![Static Badge](https://img.shields.io/badge/Christian-Garcia-orange?logo=Github&link=https%3A%2F%2Fgithub.com%2Fchristiangarcia0311)


## Contact

For issues or feature requests, please open an issue on GitHub. Contributions, feature requests, and feedback are all welcome!




