import os
import smtplib
import copy
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
import docx
from googleSheet import get_emails
import configParser
import mail
import pdfAnnounc

date = '25.11.2020'

msg = MIMEMultipart()
msg['Subject'] = 'Семінар ЦДД КАУ ' + date

headerFileName = "light.png"

pdfAnnounc.attach(msg, date)

img_data = open(headerFileName, 'rb').read()
image = MIMEImage(img_data, name=os.path.basename(headerFileName))
image.add_header('Content-ID', '<{}>'.format(headerFileName))
part2 = MIMEText(mail.create_message(), "html")

msg.attach(part2)
msg.attach(image)

mails = ['vortmanmax@gmail.com']# get_emails() 

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(configParser.getSmtpLogin(), configParser.getSmtpPassword())

sendmailStatus = smtpObj.sendmail('vortmanmax@gmail.com', mails, msg.as_string())
if sendmailStatus != {}:
    print('There was a problem sending emails.\n %s' %sendmailStatus)

smtpObj.quit
