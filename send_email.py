import smtplib, ssl

def send_email(message):
    host = "user@example.com"
    port = 465
    username = "user@example.com"
    password = 'fmifmjlgigsetsiifn'
    receiver = "user@example.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)