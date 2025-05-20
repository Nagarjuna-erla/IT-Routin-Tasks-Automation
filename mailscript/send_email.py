import smtplib
from email.message import EmailMessage

#prepare To/from subject information
email = EmailMessage()
email['from'] = 'Nagarjuna'
email['to'] = 'erlaindia@gmail.com'
email['subject'] = 'You got email from nagarjuna'


#Add E-mail body discription
#It should text/image or html link
email.set_content('I am pro in python ')


#Login to your Email account and sent mail
with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('erlanaga2@gmail.com', password='ugkXXXXXX') #If your E-mail not accepting your direct passwrod add your app-pasword
    smtp.send_message(email)                                
    print('all good boss')


