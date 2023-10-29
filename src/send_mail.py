from app.send_email import DesireContent,EmailContext
from app.settings import EMAIL_USERNAME,contacts
from app.fetch_and_write import fetch_pages

if __name__ == '__main__':

    software_context = DesireContent(title='نرم افزار')
    email_obj = EmailContext(EMAIL_USERNAME,contacts,
                             'اعلام نیاز های نرم افزاری', software_context.get_context())
    email_obj.send_email()
    software_context.tag_is_sent()