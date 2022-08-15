import smtplib
import logging
import os


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()

logger.addHandler(ch)

logger.info(__name__)



EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EAMIL_PASSWORD = os.environ.get('EAMIL_PASSWORD')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(USERNAME, PASS)
#     msg ='Subject : test \n\n\n hello gmail'
#     # smtp.sendmail(USERNAME,USERNAME,msg)