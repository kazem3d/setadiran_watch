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
contacts = ['rezaghanaty@gmail.com', 'kazem3d@gmail.com', ]


class DesireContent:
    '''
        Get content that you define in initialization of object from database
        and return it as text context
    '''

    def __init__(self, organization_name='', title=''):
        self.__select_query = select(Needs).where(Needs.is_sent == False,
                                                  Needs.org_name.contains(organization_name),
                                                  Needs.title.contains(title))
        self.__context = ''

    def __search_database(self):
        with Session(engine) as session:
            for row in session.execute(self.__select_query).scalars().all():
                self.__context += f"{row.board_name} شماره نیاز: {row.number} -- عنوان: {row.title} -- {row.org_name} -- شهر: {row.city_name} \n \n"
            session.commit()

    def get_context(self):
        self.__search_database()
        return self.__context

    def is_sent(self):
        with Session(engine) as session:
            for row in session.execute(self.__select_query).scalars().all():
                row.is_sent = True
            session.commit()



class EmailContext:
    def __init__(self, sender, receivers, subject, context):
        self.__email_message = EmailMessage()
        self.__email_message['From'] = sender
        self.__email_message['To'] = receivers
        self.__email_message['Subject'] = subject
        self.__email_message.set_content(context)

    def send_email(self):
        # print('*******',len(self.__email_message.get_content()))
        if len(self.__email_message.get_content()) > 2:  # check don't send empty massage
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                smtp.send_message(self.__email_message)


if __name__ == '__main__':
    rahdari_context = DesireContent(organization_name='راهداری')
    context = rahdari_context.get_context()
    email_obj = EmailContext(EMAIL_USERNAME, contacts,
                             'اعلام نیاز های راهداری کل کشور', context)
    email_obj.send_email()
    rahdari_context.is_sent()

    software_context = DesireContent(title='نرم افزار')
    email_obj = EmailContext(EMAIL_USERNAME, 'kazem3d@gmail.com',
                             'اعلام نیاز های نرم افزاری', software_context.get_context())
    email_obj.send_email()
    software_context.is_sent()
