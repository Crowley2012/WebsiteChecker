import urllib.request
import smtplib
import time

#Email to send messages through
email=''
password=''

#Send emails to these addresses
emails = ['9995551234@vzwpix.com']

Check = True
EmailBackup = ""
server = ""

def sendEmail(sendto):
    global EmailBackup, email, password, emails, server
    
    EmailBackup = sendto
    
    try:
        server.sendmail( email, EmailBackup, 'DayZ is out!')
    except:
        print("Error sending email.")
        time.sleep(15)
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login( email, password )
        sendEmail(EmailBackup)


def sendMessage():
    global EmailBackup, email, password, emails, server
    
    print("DayZ is out!")
    print("Sending messages...")
    
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( email, password )
    
    x = 0
    for x in range(0,6):
        sendEmail(emails[x])
        print(emails[x] + " | Success")
        x += 1

    print("Messages sent successfully.")    
    Check = False
    


def webCheck():
    global Check, EmailBackup, email, password, emails, server
    while(Check):
        try:
            with urllib.request.urlopen("http://store.steampowered.com/search/?snr=1_4_4__12&term=dayz") as site:
                test = site.read()
                try:
                    print(time.strftime("Checking for DayZ | " + "%I:%M:%S"))
                    test.index(b"1 - 7 of 7")
                    time.sleep(300)
                except:
                    Check = False
                    sendMessage()
        except:
            Check = True
            print("Error connecting to website.")
            time.sleep(60)
            webCheck()


webCheck()
