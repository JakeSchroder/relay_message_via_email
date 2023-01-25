import yagmail
import configparser
import logging

def send_message(firstName, lastName, email, message):
    config = configparser.ConfigParser()
    config.read('config.ini')
    receiver_email = "jake.schroder@gmail.com"
    body = "Name: %s %s \nEmail: %s\nMessage:\n%s" %(firstName, lastName, email, message)
    try:
        yag = yagmail.SMTP(config['EmailLogin']['sender_email'], config['EmailLogin']['sender_password'])# Log in using google app passcode

        yag.send(
            to=receiver_email,
            subject="Someone wants to linkup!",
            contents=body, 
        )
    except Exception as e:
        logging.error("Failed to send email that contained:\n%s" %(body))