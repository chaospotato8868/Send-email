import os
import smtplib
import getpass

EMAIL_ADDRESS = 'test.chao8868@gmail.com'
EMAIL_PASSWORD = getpass.getpass()

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6pm this Saturday?'
    
    msg = f'Subject:{subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS, 'dingchaoruc8868@gmail.com', msg)
