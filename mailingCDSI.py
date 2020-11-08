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

date = '11.11.2020'

msg = MIMEMultipart()
msg['Subject'] = 'Семінар ЦДД КАУ ' + date

headerFileName = "light.png"

filename='Announcement_KAU_' + date + '.pdf'
filename2 = 'Оголошення_КАУ_' + date + '.pdf'
fp=open(filename,'rb')
fp2=open(filename2,'rb')
att = MIMEApplication(fp.read(),_subtype="pdf")
att2 = MIMEApplication(fp2.read(),_subtype="pdf")
fp.close()
fp2.close()
att.add_header('Content-Disposition','attachment',filename=filename)
att2.add_header('Content-Disposition','attachment',filename=filename2)
msg.attach(att)
msg.attach(att2)

img_data = open(headerFileName, 'rb').read()
image = MIMEImage(img_data, name=os.path.basename(headerFileName))
image.add_header('Content-ID', '<{}>'.format(headerFileName))
part2 = MIMEText(mail.create_message(), "html")

msg.attach(part2)
msg.attach(image)

mails = get_emails() 

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(configParser.getSmtpLogin(), configParser.getSmtpPassword())

sendmailStatus = smtpObj.sendmail('vortmanmax@gmail.com', mails, msg.as_string())
if sendmailStatus != {}:
    print('There was a problem sending emails.\n %s' %sendmailStatus)

smtpObj.quit
