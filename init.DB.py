import sqlite3

def init():
     conn = sqlite3.connect('accounts.db')
     c = conn.cursor()
     # Create table
     c.execute('''CREATE TABLE TrustedAccounts (ID INT, mails TEXT)''')
     c.execute('''CREATE TABLE TestedAccounts (ID INT, mails TEXT)''')
     conn.commit()
     conn.close()

def fill():
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    # Fill table
    TrustedAccounts = [('1', 'test123testabc@yopmail.com'),
                ('2', 'test123testabcd@yopmail.com'),
               ]
    TestedAccounts = [('1', 'test123@gmail.com'),
                ('1', 'azerty@gmail.com'),
                ('2', 'test123@gmail.com'),
                ('2', 'azerty@gmail.com'),
               ]
    c.executemany("INSERT INTO TrustedAccounts VALUES(?, ?)", TrustedAccounts)
    c.executemany("INSERT INTO TestedAccounts VALUES(?, ?)", TestedAccounts)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init()
    fill()
