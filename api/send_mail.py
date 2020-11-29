import smtplib
from email.mime.text import MIMEText


def send_mail(athlete, email, racelinks):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '62fae0057de401'
    password = 'd2c6c6843b8a89'
    message = f'''We have a new registered user: {athlete} with email {email}
                  having race results: {racelinks}'''
    sender_email = 'example@exm.pl'
    reciever_email = 'example2@exm.pl'
    msg = MIMEText(message, 'text')
    msg['Subject'] = 'New Athlete Balkan Ultra'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    # Send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())
