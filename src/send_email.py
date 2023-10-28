import smtplib
import logging
from settings import EMAIL_PASSWORD,EMAIL_USERNAME
from email.message import EmailMessage
from src.db_config import Needs
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# ch = logging.StreamHandler()

# logger.addHandler(ch)

# logger.info(__name__)

engine = create_engine("sqlite:///sqlite.db", echo=True, future=True)






class DesireContent:
    '''
        Get content that you define in initialization of object from database
        and return it as text context
    '''

    def __init__(self, organization_name='', title=''):
        self.__organization_name = organization_name
        self.__title = title
        self.__context = ''

    def __search_database(self):
        with Session(engine) as session:
            stmt = select(Needs).where(Needs.is_sent == False,
                                       Needs.org_name.contains(
                                           self.__organization_name),
                                       Needs.title.contains(self.__title))
            for row in session.execute(stmt).scalars().all():
                self.__context += f"{row.board_name} شماره نیاز: {row.number} -- عنوان: {row.title} -- {row.org_name} -- شهر: {row.city_name} \n \n"
            session.commit()

    def get_context(self):
        self.__search_database()
        return self.__context

    def tag_is_sent(self):
        with Session(engine) as session:
            stmt = select(Needs).where(Needs.is_sent == False,
                                       Needs.org_name.contains(
                                           self.__organization_name),
                                       Needs.title.contains(self.__title))
            for row in session.execute(stmt).scalars().all():
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
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()  # send the extended hello to our server
                smtp.starttls()  # tell server we want to communicate with TLS encryption
                smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                smtp.send_message(self.__email_message)


