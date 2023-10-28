import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
contacts = ['list-of-email']