from os import listdir
from email.mime.application import MIMEApplication
from seminarDate import nextWednesdayDateInStandardFormat

def attach(msg):
    files = [f for f in listdir('./data/') if f.endswith(nextWednesdayDateInStandardFormat + '.pdf')]
    for f in files:
        with open('./data/' + f, 'rb') as fp:
            att = MIMEApplication(fp.read(),_subtype="pdf")
        att.add_header('Content-Disposition','attachment',filename=f)
        msg.attach(att)