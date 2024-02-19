import smtplib
import ssl
from email.message import EmailMessage


def send_mail(user_email, user_name, user_query, user_message):
    host = "smtp.gmail.com"
    port = 465

    # Replace the username, password and receiver credentials
    username = "SENDER_EMAIL"
    password = "SENDER_PASSWORD"

    receiver = "RECEIVER_EMAIL"
    context = ssl.create_default_context()

    # Composing the mail format
    msg = EmailMessage()
    msg.set_content(f"Name: {user_name}\nEmail: {user_email}\n"
                    f"Query: {user_query}\n\nMessage: {user_message}")
    msg['Subject'] = 'Someone wants to get in touch!'
    msg['From'] = username
    msg['To'] = receiver

    # Running the mail server
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)
        server.quit()
