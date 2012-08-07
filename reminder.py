#!/usr/bin/env python
import smtplib
import csv
import os
import logging
from datetime import datetime, timedelta
from ConfigParser import SafeConfigParser


SMTP_SERVER  = 'smtp.gmail.com'
SMTP_PORT = 587
ACCOUNT_FILE = "account.txt"
MAILSLIST = 'mails.csv'
DATEFILE = 'last_check.txt'

log = logging.getLogger("reminder")

def read_account(filename):
    conparser = SafeConfigParser()
    conparser.read(filename)
    user = conparser.get('account', 'username')
    password = conparser.get('account', 'password')
    return (user, password)


def send_mail(recipient, subject, body):
    str_all_mails = ', '.join(recipient)
    sender, passwd = read_account(ACCOUNT_FILE)
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
    smtp.login(sender, passwd)
    
    body = "" + body +""
    smtp.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    log.info("Sent mail to %s", recipient)
    print "Sent to ", 
    print recipient
    smtp.quit()


def send_happybirthday(recipient):
    log.info("Send happy birthday to %s", recipient)
    body = """Happy birthday to you!
            \n<br/>From C2k8pro with love
            \n<br/>http://c2.familug.org"""
    subject ='[BirthReminder] Happy birthday to you! from C2k8pro'
    send_mail(recipient, subject, body)


def send_notification(all_mails, names):
    log.info("Tomorrow is birthday of %s", names)
    tomorrow = get_next_day_str(datetime.now())
    body = """Tomorrow (%s) is birthday of %s""" % (tomorrow, names)
    send_mail(all_mails, body,  body)


def convert_to_string(date):
    str_format = "%d/%m"
    return date.strftime(str_format)


def get_next_day_str(today):
    one_day = timedelta(days=1)
    tomorrow = today + one_day
    return convert_to_string(tomorrow)


def read_csv():
    NAME_IDX = 1
    DOB_IDX = 2
    MAIL_IDX = 3

    try:
        reader = csv.reader(open(MAILSLIST, 'rt'), delimiter=',')
    except IOError, e:
        print "PLEASE PLACE YOUR CSV DATA FILE TO THIS DIRECTORY"
    else:
        all_mails = []
        today = datetime.now()
        str_today = convert_to_string(today)
        str_tomorrow = get_next_day_str(today)

        print 'Today is ', str_today
        tomorrow_birth = []

        for row in reader:
            name = row[NAME_IDX].strip()
            dob = row[DOB_IDX]
            dmy = dob.split("/")
            mail = row[MAIL_IDX]
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
        print '%s mails: ' % len(all_mails)

        if tomorrow_birth:
            all_tomorrow = ', '.join(tomorrow_birth)
            send_notification(all_mails, all_tomorrow)
        

def main():
    LOG_PATH = "birthreminder.log"
    logging.basicConfig(level=logging.DEBUG, filename=(os.path.abspath(LOG_PATH)), 
                format="%(asctime)s %(name)s %(levelname)s %(message)s",)
    log.info("Checked")
    read_csv()


if __name__ == "__main__":
    main()
