import smtplib
from email.mine.text import MIMEText
from email.mime.multipart import MIMEMultipart


username ='moodsync0@gmail.com'
password='ihate@mypassword#'


def send_mail(text='Email Body', subject='Hello World', from_email= 'moodsync0 <moodsync0@gmail.com>', to_emails=None):
  assert isinstance(to_emails, list)
  msg = MIMEMultipart('alternative')
  msg['From'] = from_email
  msg['To'] = ", "

  msg_str=""
    # login to my smtp server
  server = smtplib.SMTP(host='smtp.gmail.com', port=587)
  server.ehlo()
  server.starttls()
  server.login(username, password)
  server.send(from_email, to_emails, msg_str)
  server.quit()
    #with smtplib.SMTP() as server:
    # server.login(username, password)
    # pass
