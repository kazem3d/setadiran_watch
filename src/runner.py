import sys
from app.fetch_and_write import fetch_pages
from app.send_email import DesireContent,EmailContext
from app.settings import EMAIL_USERNAME,contacts

if __name__ == '__main__':
    if sys.argv[1:] in (["--fetch"],):
        fetch_pages(50)
    elif sys.argv[1:] in (["--mail"],):
        software_context = DesireContent(title='نرم افزار')
        email_obj = EmailContext(EMAIL_USERNAME,contacts,
                                'اعلام نیاز های نرم افزاری', software_context.get_context())
        email_obj.send_email()
        software_context.tag_is_sent()
    else:
        sys.stdout.write('use --fetch to fetch data and save in database' + '\n')
        sys.stdout.write('use --mail to set data as email' + '\n')