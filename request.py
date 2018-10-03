import requests
import smtplib
from email.message import EmailMessage
import json
import sqlite3

def request(mail):
    # Testing mail on the HaveIBeenPwned API
    print("Testing : " + mail)
    url = ('https://haveibeenpwned.com/api/v2/breachedaccount/' +  mail)
    r = requests.get(url)
    if r.status_code == 200:
        results = r.json()
        return(results)
    else:
        return None

def alerting(results, TrustedAccount, TestedAccount):
    # Sending mail when detecting something, nothing otherwise
    SERVER = "localhost"
    FROM = "root@example.com"
    TO = TrustedAccount
    SUBJECT = "/!\\ Alert /!\\ Breach found on the following address: " + TestedAccount
    TEXT = "If you receive this email, the account: " + TestedAccount + " has been potentially hacked. I suggest you to modify your password. Please, find bellow the site that has been hacked and where your account leaked: \n\n"
    for result in results:
        TEXT += result["Name"]+": (Domain: "+result["Domain"]+")" " has been hacked in "+result["BreachDate"]+".\n"

    message = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (FROM, TO, SUBJECT, TEXT)

    server = smtplib.SMTP(SERVER)
    server.set_debuglevel(3)
    server.sendmail(FROM, TO, message)

def getTrustedAccounts():
    conn = sqlite3.connect("accounts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM TrustedAccounts")
    rows = c.fetchall()
    conn.close()
    return rows

def getTestedAccounts():
    conn = sqlite3.connect("accounts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM TestedAccounts")
    rows = c.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    TrustedAccounts = getTrustedAccounts()
    TestedAccounts = getTestedAccounts()
    for TrustedAccount in TrustedAccounts:
        for TestedAccount in TestedAccounts:
            if TestedAccount[0] == TrustedAccount[0]:
                alert = request(TestedAccount[1])
                if alert == None:
                    print('No breach found for address: '+TestedAccount[1])
                    continue
                else:
                    alerting(alert, TrustedAccount[1], TestedAccount[1])
