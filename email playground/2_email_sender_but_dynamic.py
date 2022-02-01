import smtplib  # (Simple Mail Transfer Protocol) server that communicates the language of the email
from email.message import EmailMessage
# New Modules be Like: "Allow Us To Introduce Ourselves!"
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())  # Wrapping the path in Template to use as a substitute
email = EmailMessage()
email['from'] = 'Blue Bird'
email['to'] = 'BlackClover1003@gmail.com'
email['subject'] = 'Reminder'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')  # wrapping with {} as a dictionary

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('m4mubassir2@gmail.com', 'asifmubassir202016032')
    smtp.send_message(email)
    print('All Good Boss!')

# Do not name your file as email.py. It'll give you error.
# The Mail will go to the spam section! :)
