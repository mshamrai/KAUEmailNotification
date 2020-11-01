import configparser

configfile = 'config.cfg'

config = configparser.ConfigParser()
config.read(configfile)

def getSmtpLogin():
    return config['SMTP_CREDENTIALS']['login']

def getSmtpPassword():
    return config['SMTP_CREDENTIALS']['password']