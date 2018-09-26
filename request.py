import requests
import smtplib
from email.message import EmailMessage

def getMails():
    # Get Mails from mails.txt
    with open("mails.txt", "r") as f :
        content = f.read().splitlines()
    #for mail in content:
    #    print(mail)
    return content

def request(mails):
    # Testing mails from mails.txt
    for mail in mails:
        print("Testing : " + mail)
        url = ('https://haveibeenpwned.com/api/v2/breachedaccount/' +  mail)
        print(url)
        r = requests.get(url)
        print(r.text)

def alerting():
    # Sending mail when detecting something, nothing otherwise
    SERVER = "localhost"
    FROM = "root@example.com"
    TO = ["test123testabc@yopmail.com"]
    SUBJECT = "Alert !"
    TEXT = "test"

    message = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER)
    server.set_debuglevel(3)
    server.sendmail(FROM, TO, message)
    quit()

if __name__ == "__main__":
    #request(getMails())
    alerting()
