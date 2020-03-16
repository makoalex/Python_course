import smtplib
import os
from email.message import EmailMessage  # we import this so we make the code a bit more cleaner
import imghdr

email = os.environ.get('EMAIL_ADDRESS')
password = os.environ.get('EMAIL_PASSWORD')
"""instead of creating different parts of the email and then combining them, we will set them on an object we create"""
"""if we want to create an attachment we have to import the IMGHDR module"""
message = EmailMessage()  # created an message object
message['Subject'] = 'Check out this chubby puppy'
message['From'] = email
message['To'] = 'macovei.a2@gmail.com'
message.set_content('image attachemnt')
path =r"C:\Users\Mako\Desktop\Ny mappe\chubby_puppy.jpg"

with open(path, 'rb') as file:
    new_file = file.read()
    file_type = imghdr.what(file.name)
    file_name = file.name  # should return the name of the file
message.add_attachment(new_file, maintype='image', subtype=file_type, filename='chubbs')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(email, password)
    server.send_message(message)
    server.quit()
