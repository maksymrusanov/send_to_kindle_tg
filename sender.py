import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from fileinput import filename

from dotenv import load_dotenv

load_dotenv("send_to_kindle.env")


async def send_email(receiver_email, filename):
    fromaddr = os.getenv("SENDER_EMAIL")
    toaddr = receiver_email
    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = filename
    pdf = MIMEApplication(open(f"books/{filename}", "rb").read())
    pdf.add_header("Content-Disposition", "attachment", filename=filename)
    msg.attach(pdf)
    try:
        with smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT")) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(fromaddr, password=os.getenv("SMTP_PASSWORD"))
            smtpObj.sendmail(fromaddr, toaddr, msg.as_string())
    except Exception as e:
        print(e)
