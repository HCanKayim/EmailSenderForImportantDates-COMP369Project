from datetime import datetime
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "huseyincan.kayim@std.yeditepe.edu.tr"
SENDER_PASSWORD = "539lirnvva"
RECIPIENT_EMAIL = "cankayim2001@outlook.com"

def send_email(event_name):
    subject = f"{event_name}"
    body = f"""
    Merhaba,

    {event_name} kutlu olsun.

    En iyi dileklerimle,
    Hüseyin Can Kayım
    """

    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = RECIPIENT_EMAIL
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message.as_string())
            print(f"Email sent for {event_name}!")
    except Exception as e:
        print(f"Failed to send email for {event_name}: {e}")

with open("/home/ck/Desktop/Projects/369/data.json", 'r') as f:
    data = json.load(f)

today = datetime.now().strftime("%d %B").upper()

for event in data:
    if event['date'].upper() == today:
        send_email(event['name'])
