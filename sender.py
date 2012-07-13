#!/usr/bin/env python
import smtplib
from datetime import datetime

SMTP_SERVER  = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'bot.c2k8pro@gmail.com'
subject ='[BirthReminder] Happy birthday to you! from C2k8pro'
password = 'xxxx@@@'


def send_happy_birthday(recipient, body):
    """
    Send happy bithday mail
    """
    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    
    headers = "\r\n".join(headers) 
    
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(sender, password)
    
    body = "" + body +""
    smtp.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    print "Sent"
    smtp.quit()

happybirthday_body = """Happy birthday to you!
        \n<br/>From C2k8pro with love
        \n<br/>http://c2.familug.org'"""

notify_body = """Tomorrow is birthday of """

recipients = ['bot.c2k8pro@gmail.com']



today = datetime.now()
format = "%d-%m-%Y"
print today
today_in_str = datetime.strftime(today, format)

tomorrow = today + 

tomorrow_in_str = datetime.strftime(tomorrow, format)

all_mails = []
#get all mail from cvs use list comprehension

for line in csv:
    #append all mail
    if tomorrow_in_str == date_read_from_csv:
        #send notify mail to all member in clas
        for recipient in all_mails:
            send_happy_birthday(recipient, notify_body + #his/her name)
        
    if today_in_str == date_read_from_csv:
        #Send happy birthday to him/her
        send_happy_birthday(#her mail, happybirthday_body)
        


