import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
from fileinput import filename


async def send_email(receiver_email, filename):
    fromaddr =os.getenv('USER_EMAIL')
    toaddr = receiver_email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = filename
    pdf = MIMEApplication(open(f'books/{filename}', 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment',filename=filename)
    msg.attach(pdf)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(fromaddr, password=os.getenv('APP_PASSWORD'))
            smtpObj.sendmail(fromaddr, toaddr, msg.as_string())
    except Exception as e:
        print(e)


