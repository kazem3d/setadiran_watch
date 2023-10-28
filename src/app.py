from send_email import DesireContent,EmailContext
from settings import EMAIL_USERNAME,contacts


if __name__ == '__main__':


    software_context = DesireContent(title='نرم افزار')
    email_obj = EmailContext(EMAIL_USERNAME,contacts,
                             'اعلام نیاز های نرم افزاری', software_context.get_context())
    email_obj.send_email()
    software_context.tag_is_sent()