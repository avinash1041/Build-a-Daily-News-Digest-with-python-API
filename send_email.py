import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    
    username ="avijadhav1923@gmail.com"
    password = "**********"
    
    receiver = "jadhavavinash1041@gmail.com"
    content = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=content) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)