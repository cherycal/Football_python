__author__ = 'chance'

import datetime
import random
import smtplib
import time
from email.message import EmailMessage


def get_emails():
    emails = {
        "Chance": "chance_st@yahoo.com",
        "Cheryll": "cherycal@yahoo.com",
        "Reg": "8504496736@vtext.com",
        "Chris": "christiecalaycay@yahoo.com",
        "Lu": "lulucalaycay@yahoo.com",
        "JL": "jean_luc_leblanc@yahoo.com"
    }
    return emails


def confirm(mail_obj, email, time_stamp):
    msg = EmailMessage()
    msg['Subject'] = "Secret Santa Confirm"
    msg['From'] = "ccrlyclhn@gmail.com"
    msg['To'] = "chance_st@yahoo.com"
    message_text = f"Sent mail to {email} at {time_stamp}"
    msg.set_content(message_text)
    mail_obj.sendmail("ccrlyclhn@gmail.com", "chance_st@yahoo.com", str(msg))


def send_it(mail_obj, recipient_name=None, santa_email=None):
    lucky_number = random.randint(1, 29)
    msg = EmailMessage()
    msg['Subject'] = "Secret Santa"
    msg['From'] = "ccrlyclhn@gmail.com"
    msg['To'] = santa_email
    time_stamp = datetime.datetime.now().strftime('%Y%m%d - %H%M%S')

    if santa_email == "8504496736@vtext.com":
        message_text = f"You got: {recipient_name}\n\nLucky number: {lucky_number}\n\nSent at {time_stamp}"
    else:
        message_text = f"You got: {recipient_name}\n\nSent at {time_stamp}"

    msg.set_content(message_text)
    # print(f"Message:\n{msg}\n\n")

    if santa_email == "chance_st@yahoo.com" or False:
        mail_obj.sendmail("ccrlyclhn@gmail.com", santa_email, str(msg))

    confirm(mail_obj, santa_email, time_stamp)

    time.sleep(.2)


def generate_non_matching_permutation(lst):
    while True:
        shuffled = lst[:]
        random.shuffle(shuffled)
        if all(a != b for a, b in zip(lst, shuffled)):
            return shuffled


def send_from_list():
    mail_obj = create_mail_object()
    email_list = ["8504496736@vtext.com", "chance_st@yahoo.com", "6463916024@vtext.com", "9175896042@vtext.com"]
    for email in email_list:
        send_it(mail_obj, "A Secret Santa Test Message", email)
        time.sleep(5)
    mail_obj.quit()


def create_mail_object():
    mail_obj = smtplib.SMTP('smtp.gmail.com', 587)
    mail_obj.starttls()
    mail_obj.login("ccrlyclhn@gmail.com", "xwwu riwd rsge piie")
    return mail_obj


def main():
    mail_obj = create_mail_object()
    emails = get_emails()
    santas = list(emails.keys())
    recipients = generate_non_matching_permutation(santas)
    for santa, recipient in zip(santas, recipients):
        send_it(mail_obj, recipient_name=recipient, santa_email=emails[santa])
    mail_obj.quit()


if __name__ == "__main__":
    main()
