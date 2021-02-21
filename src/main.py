from seminarDate import nextWednesdayDateInStandardFormat
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from googleSheet import get_emails
import pdfAnnounc
import smtplib
import mail
import os



SMTP_LOGIN = os.environ.get('SMTP_LOGIN')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
TEST_EMAIL = os.environ.get('TEST_EMAIL')
DATE = nextWednesdayDateInStandardFormat
HEADER_FILENAME = "light.png"


def build_msg():
    msg = MIMEMultipart()
    msg['Subject'] = 'Семінар ЦДД КАУ ' + DATE
    pdfAnnounc.attach(msg)
    img_data = open('./data/' + HEADER_FILENAME, 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename(HEADER_FILENAME))
    image.add_header('Content-ID', '<{}>'.format(HEADER_FILENAME))
    msg.attach(MIMEText(mail.create_message(), "html"))
    msg.attach(image)
    
    return msg


def send_to_emails(msg, mails):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(SMTP_LOGIN, SMTP_PASSWORD)

    sendmailStatus = smtpObj.sendmail(SMTP_LOGIN, mails, msg.as_string())
    if sendmailStatus != {}:
        print('There was a problem sending emails.\n %s' %sendmailStatus)
    smtpObj.quit


if __name__ == '__main__':
    message = build_msg()
    if TEST_EMAIL:
        emails = [TEST_EMAIL]
    else:
        emails = get_emails()
    send_to_emails(message, emails)
