# HaveIBeenPwned
Automatically check and alert user if breach found on haveibeenpwned.com

# How to init the Database ?
The database contains two tables : One named TrustedAccount, which contain all the account where the alerts will be send, and another one named TestedAccount which contains all the accounts to test on the HaveIBeenPownd API. Following is the default database. You have to modify the file initDB.py to enter the addresses you want to test:
## Table TrustedAccounts
| ID | mails |
| --- | --- |
| 1 | test123testabc@yopmail.com |
| 2 | test123testabcd@yopmail.com |
| 3 | test123testabcde@yopmail.com |

## Table TestedAccounts
| ID | mails |
| --- | --- |
| 1 | test123@gmail.com |
| 1 | azerty@gmail.com |
| 2 | test123@gmail.com |
| 2 | azerty@gmail.com |
| 3 | s12425djkfslkdjfvslkjdf@gmail.com |
| 3 | azerty@gmail.com |
