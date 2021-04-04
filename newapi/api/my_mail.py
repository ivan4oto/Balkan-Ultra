import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from newapi.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

context = ssl.create_default_context()


def my_mail_send(reciever, subject, body):
    # Try to log in to server and send email
    recievers = ['balkanultra@abv.bg']
    recievers.append(reciever)
    msg = MIMEMultipart()
    msg['FROM'] = EMAIL_HOST_USER
    msg['To'] = reciever
    msg['Subject'] = subject
    body = MIMEText(body, 'plain')
    msg.attach(body)

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER, recievers, msg.as_string())

