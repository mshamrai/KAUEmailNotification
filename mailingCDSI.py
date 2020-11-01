import os
import smtplib
import copy
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
import docx
from google_sheet import get_emails
import configParser

date = '04.11.2020'

msg = MIMEMultipart()
msg['Subject'] = 'Семінар ЦДД КАУ ' + date


headerFileName = "light.png"

html = """\
   
<div style="height:100%;margin:0;padding:0;width:100%;background-color:#fafafa">
<center>
    <table id="m_8632786949691406836bodyTable" style="height:100%;border-collapse:collapse;margin:0;padding:0;width:100%;background-color:#fafafa" width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
        <tbody><tr>
            <td id="m_8632786949691406836bodyCell" style="height:100%;margin:0;padding:10px;width:100%;border-top:0" valign="top" align="center">
                
                
                <table style="border-collapse:collapse;border:0;max-width:600px!important" width="100%" cellspacing="0" cellpadding="0" border="0">
                    <tbody><tr>
                        <td id="m_8632786949691406836templatePreheader" style="background-color:#fafafa;background-image:none;background-repeat:no-repeat;background-position:center;background-size:cover;border-top:0;border-bottom:0;padding-top:9px;padding-bottom:9px" valign="top">
                            <img src="cid:light.png" width="865" height="289">
                        </td>   
                    </tr>
                    <tr>
                        <td id="m_8632786949691406836templateHeader" style="background-color:#ffffff;background-image:none;background-repeat:no-repeat;background-position:center;background-size:cover;border-top:0;border-bottom:0;padding-top:9px;padding-bottom:0" valign="top">
                            <table style="min-width:100%;border-collapse:collapse" width="100%" cellspacing="0" cellpadding="0" border="0">
                                <tbody>
                                <tr>
                                    <td style="padding-top:9px" valign="top">
                                        

                                        
                                        <table style="max-width:100%;min-width:100%;border-collapse:collapse" width="100%" cellspacing="0" cellpadding="0" border="0" align="left">
                                            <tbody>
                                            <tr>
                                                <td style="padding-top:0;padding-right:18px;padding-bottom:9px;padding-left:18px;word-break:break-word;color:#202020;font-family:Helvetica;font-size:16px;line-height:150%;text-align:left" valign="top">
                                                    <center><i>You can find an english version of this announcement in the attachment to this message</i></center>
                                                    <p>Шановні колеги!&nbsp;</p>                                                   
                                                    <p>Запрошуємо Вас на черговий робочий семінар Центру дослідження даних Київського академічного університету.</p>
                                                    <ul>
                                                    <li><p><b>Доповідач:</b> Ємельянов Михайло Олексійович
                                                        <br/>
                                                        (студент Київського Академічного Університету)
                                                    </p>
                                                    <p><b>Тема:</b> Дослідження web-форуму як соціокультурного феномену та використання сучасних скриптових мов
                                                    програмування для створення інтернет форуму студентів</p>
                                                    <p> Сьогодні все більшого значення набуває інформатизація освіти та розробка методичних системи, технологій, 
                                                    методів і організаційних форм навчання, що дозволяють удосконалити механізм управління системою освіти 
                                                    в сучасних умовах інформаційного суспільства. Основними інтернет-технологіями, що використовуються в 
                                                    освітніх цілях, є засоби синхронної та асинхронної комунікації. У даному дослідженні був розглянутий 
                                                    інтернет-форум, як засіб асинхронної комунікації. У ході дослідження була побудована та описана 
                                                    концептуальна модель інтернет-форуму, визначені роль і перспективи інтернет-спільнот типу «форум» в 
                                                    соціокультурній системі сучасного інформаційного суспільства, а також спроектований та програмно 
                                                    реалізований прототип студентського web-форуму.</p>
                                                    </li>
                                                    </ul>
                                                    <p><b>Коли:</b> 4 листопада (середа) о 17:00</p>
                                                    <p><b>Де:</b> <a href="https://us02web.zoom.us/j/81901090493?pwd=bkVlOVBJWEJMcFdNMDNOc2liUkNRUT09">конференція в Zoom</a></p>
                                                    <p>За оновленою інформацією слідкуйте на сайті
                                                        <a href="https://sites.google.com/view/data-analysis/home">ЦДД КАУ</a>,
                                                        або на сторінці <a href="https://kau.org.ua/deps/math/251-seminar-tsentru-doslidzhennia-danykh-ta-innovatsii"> кафедри математики KAU.</a></p>
                                                        <p>Також інформація про оновлені семінари розташовується на сайті 
                                                            <a href="https://www.imath.kiev.ua/events/index.php?seminarId=96">Інституту математики НАН України</a></p>
                                                    <p>
                                                        З повагою,
                                                    </p>
                                                    <p>
                                                        Керівники семінару: <br/>
                                                        Антонюк Олександра Вікторівна,<br/>
                                                        Сенько Іван Олександрович
                                                    </p>
                                                    <p>
                                                        Наукові секретарі семінару: <br/>
                                                        Максим Шамрай,<br/>
                                                        Марина Караванська
                                                    </p>
                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>
                                        
                                        
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody></table>
                
                
            </td>
        </tr>
    </tbody></table>
</center>
</div>
"""

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
part2 = MIMEText(html, "html")


img_data = open(headerFileName, 'rb').read()
image = MIMEImage(img_data, name=os.path.basename(headerFileName))
image.add_header('Content-ID', '<{}>'.format(headerFileName))
part2 = MIMEText(html, "html")

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
