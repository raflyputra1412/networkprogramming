#Muhammad Rafly Hersa Putra
#170010009

import getpass
import poplib
import imaplib

IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993

POP_SERVER = 'pop.gmail.com'
POP_PORT = 995


def imap_mail(username):
        mailbox = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        password = getpass.getpass(prompt='Enter your email password: ')
        mailbox.login(username[0], password)
        mailbox.select('Inbox')
        typ, data = mailbox.search(None, 'ALL')
        for num in data[0].split():
            typ, data = mailbox.fetch(num, '(RFC822)')
            print ('Message %s\n%s\n' % (num, data[0][1]))
            break
        mailbox.close()
        mailbox.logout()

def pop_mail(username):
        mailbox = poplib.POP3_SSL(POP_SERVER, POP_PORT)
        mailbox.user(username[0])
        password = getpass.getpass(prompt='Enter your email password: ')
        mailbox.pass_(password)
        num_messages = len(mailbox.list()[1])
        print ('Total emails: {}'.format(num_messages))
        mailbox.quit()


def mail(username, protocol, host, port):
    data = [username, protocol, host, port]
    if (protocol == 1):
        imap_mail(data)

    elif (protocol == 2):
        pop_mail(data)

username = input("input email: ")
try:
    print("type 1 for imap or type 2 for pop3.")
    protocol = int(input("protocol: "))
except:
    print("hmm there is something wrong here...")

mail(username, protocol, host, port)