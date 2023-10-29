from app.send_email import DesireContent,EmailContext
from app.settings import EMAIL_USERNAME,contacts
from app.fetch_and_write import fetch_pages

if __name__ == '__main__':

    fetch_pages(50)
