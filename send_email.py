import yagmail

def send_message(firstName, lastName, email, message):
    receiver_email = "jake.schroder@gmail.com"
    sender_email = "bot@gmail.com"
    body = "Name: %s %s \nEmail: %s\nMessage:\n%s" %(firstName, lastName, email, message)
    yag = yagmail.SMTP(sender_email)
    
    yag.send(
        to=receiver_email,
        subject="Someone wants to linkup!",
        contents=body, 
    )