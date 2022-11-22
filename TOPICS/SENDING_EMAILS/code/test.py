import smtplib

# sender email
sender: str = 'boodyfortest@gmail.com'

# receiver email
receiver: str = 'abdelrahmanahmedhamdy99@gmail.com'

# password for sender email
password: str = ''  # place the password here

# subject of the email
subject: str = 'testing sending emails'

# body of the email
body: str = 'this is a test email sent by python script'


# message will be sent
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

# let's create a server object
server = smtplib.SMTP("smtp.gmail.com", 587)

# start layer security
server.starttls()

# login to sender email
server.login(sender, password)

print('logged in')

print("sending email....")
# let's send the email
server.sendmail(sender, receiver, message)

print("email was sent successfully")
