#!/usr/bin/env python
import smtplib
import csv
from datetime import datetime, timedelta

SMTP_SERVER  = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'bot.c2k8pro@gmail.com'

password = None
with open('pass', 'rt') as f:
    password = f.read().strip('\n')


def send_mail(recipient, subject, body):
    str_all_mails = ', '.join(recipient)
    """
    Send happy bithday mail
    """
    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + str_all_mails,
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
    print "Sent to ", 
    print recipient

    smtp.quit()

def send_happybirthday(recipient):
    body = """Happy birthday to you!
            \n<br/>From C2k8pro with love
            \n<br/>http://c2.familug.org"""
    subject ='[BirthReminder] Happy birthday to you! from C2k8pro'
    send_mail(recipient, subject, body)


def send_notification(all_mails, names):
    body = """Tomorrow is birthday of %s""" % names
    send_mail(all_mails, body,  body)


def read_csv():
    FILENAME = 'mails.csv'
    reader = csv.reader(open(FILENAME, 'rt'), delimiter=',')

    today = datetime.now()
    one_day = timedelta(days=1)
    tomorrow = today + one_day

    all_mails = []
    str_format = "%d/%m"
    str_today = today.strftime(str_format)
    str_tomorrow = tomorrow.strftime(str_format)

    print 'Today is ', str_today
    tomorrow_birth = []
    for row in reader:
        name = row[1].strip()
        dob = row[2]
        dmy = dob.split("/")
        mail = row[3]
        all_mails.append(mail)

        #TODO fix dob with only 1 digit
        birth_date = dmy[0] + "/" + dmy[1]
        if str_today == birth_date:
            print 'Happy birthday %s' % name

            try:
                send_happybirthday(mail)
            except Exception, e:
                print e

        elif str_tomorrow == birth_date:
            tomorrow_birth.append(name)
            print "Tomorrow is %s's birthday" % name

    # Remove empty string
    all_mails = filter(None, all_mails)
    #all_mails = ['hvnsweeting@gmail.com']
    #all_mails.append('bot.c2k8pro@gmail.com')
    print 'All mails: ', len(all_mails)

    if tomorrow_birth:
        all_tomorrow = ', '.join(tomorrow_birth)
        send_notification(all_mails, all_tomorrow)
        

def main():
    read_csv()

if __name__ == "__main__":
    main()

