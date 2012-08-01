#!/usr/bin/env python
import smtplib
import csv
from datetime import datetime, timedelta

SMTP_SERVER  = 'smtp.gmail.com'
SMTP_PORT = 587
ACCOUNT_FILE = "account.txt"


def read_account(filename):
    with open(filename, 'rt') as f:
        sender  = f.read().strip()
        password = f.read().strip()
    return (sender, password)


def send_mail(recipient, subject, body):
    str_all_mails = ', '.join(recipient)
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
    smtp.login(read_account(ACCOUNT_FILE))
    
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
    FILENAME = 'mails.csv'
    reader = None
    try:
        reader = csv.reader(open(FILENAME, 'rt'), delimiter=',')
    except IOError, e:
        print "Please place your csv data file to this directory"

    else:
        all_mails = []
        today = datetime.now()
        str_today = convert_to_string(today)
        str_tomorrow = get_next_day_str(today)

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
        print '%s mails: ' % len(all_mails)

        if tomorrow_birth:
            all_tomorrow = ', '.join(tomorrow_birth)
            send_notification(all_mails, all_tomorrow)
        

def main():
    read_csv()

if __name__ == "__main__":
    main()

    # NOTE : not test
