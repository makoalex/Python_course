import smtplib
import os

email = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('EMAIL_PASSWORD')
recipient = 'olovholm @gmail.com'
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)
    subjet ='din-din?'
    body ='wanna have dinner later?'
    message = 'Subject: {}\n\n{}'.format(subjet, body)
    server.sendmail(email, recipient, message)
    server.quit()



