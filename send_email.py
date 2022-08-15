import smtplib
import logging
import os
from email.message import EmailMessage
from db_config import Needs
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()

# logger.addHandler(ch)

# logger.info(__name__)

engine = create_engine("sqlite:///sqlite.db", echo=True, future=True)


EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
contacts = ['rezaghanaty@gmail.com','kazem3d@gmail.com',]



# _________________________________________________ راهداری


with Session(engine) as session:
    context =''
    stmt = select(Needs).where(Needs.is_sent == False,Needs.org_name.contains('راهداری'))
    for row in  session.execute(stmt).scalars().all():
        context +=f"{row.board_name} شماره نیاز: {row.number} -- عنوان: {row.title} -- {row.org_name} -- شهر: {row.city_name} \n \n"
        row.is_sent = True
    session.commit()


msg_rmto = EmailMessage()
msg_rmto['From'] = EMAIL_USERNAME
msg_rmto['To'] = contacts
msg_rmto['Subject'] = 'اعلام نیاز های راهداری کل کشور'
msg_rmto.set_content(context)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    # smtp.sendmail(EMAIL_USERNAME,EMAIL_PASSWORD,'test')
    smtp.send_message(msg_rmto)


# _______________________________________  شهرداری


with Session(engine) as session:
    context =''
    stmt = select(Needs).where(Needs.is_sent == False,Needs.org_name.contains('شهرداری'),Needs.province_name.contains('مرکز'))
    for row in  session.execute(stmt).scalars().all():
        context +=f"{row.board_name} شماره نیاز: {row.number} -- عنوان: {row.title} -- {row.org_name} -- شهر: {row.city_name} \n \n"
        row.is_sent = True
    session.commit()



msg_shahr = EmailMessage()
msg_shahr['From'] = EMAIL_USERNAME
msg_shahr['To'] = contacts
msg_shahr['Subject'] = 'اعلام نیاز های شهرداری استان'
msg_shahr.set_content(context)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
    smtp.send_message(msg_shahr)

