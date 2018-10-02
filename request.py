import requests
import smtplib
from email.message import EmailMessage
import json

def request(mail):
    # Testing mail on the HaveIBeenPwned API
    print("Testing : " + mail)
    url = ('https://haveibeenpwned.com/api/v2/breachedaccount/' +  mail)
    print(url)
    r = requests.get(url)
    results = r.json()
    return(results)

def alerting(results, mail):
    # Sending mail when detecting something, nothing otherwise
    SERVER = "localhost"
    FROM = "root@example.com"
    TO = ["test123testabc@yopmail.com"]
    SUBJECT = "/!\\ Alert /!\\ Breach found on the following address: " + mail
    TEXT = "If you receive this email, the account: " + mail + " has been potentially hacked. I suggest you to modify your password. Please, find bellow the site that has been hacked and where your account leaked: \n\n"
    for result in results:
        TEXT += result["Name"]+": (Domain: "+result["Domain"]+")" " has been hacked in "+result["BreachDate"]+".\n"

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
    # Get Mails from mails.txt
    with open("mails.txt", "r") as f :
        mails = f.read().splitlines()
    for mail in mails:
        alert = request(mail)
        alerting(alert, mail)
