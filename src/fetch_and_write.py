import requests
import json
from src.db_config import Needs
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
import time
import logging
from settings import BASE_DIR




logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch = logging.FileHandler(BASE_DIR / 'loggs.log')
st = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(st)


headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,an;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://fe.setadiran.ir',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

break_counter = 0

for page in range(0,50):
    time.sleep(4)
    logger.info(f'reading page {page}')


    response = requests.get(f'https://gw.setadiran.ir/api/centralboard/cards/?searchTypeCode=0&boardCode=2,1,3&tagCode=4121,4130,4128,4120,4123,4134,1442,1441,31,32,33,34,35&queryText=&pageNumber={page}&pageSize=10&sort=insertDate,desc', headers=headers)
    
    if response.status_code != 200 :
        logger.error(f'Error in fetch data - error {response.status_code}')
        break
    data=json.loads(response.text)
    data = data['content']

    engine = create_engine("sqlite:///sqlite.db", future=True)

    with Session(engine) as session:
        for row in data :
            if session.query(exists().where(Needs.number == row['number'])).scalar() == True :
                logger.info('*******duplicate*********')
                break_counter += 1
                break
            else :
                break_counter = 0

            insert_dict={
                'number' : row['number'],
                'title' : row['title'],
                'org_name' : row['orgName'],
                'city_name' : row['cityName'],
                'province_name' : row['provinceName'],
                'board_name' : row['boardName'],
                'jalali_send_deadline' :row['jalaliSendDeadlineDate'],
                'jalai_document_deadline' :row['jalaliDocumentDeadlineDate'],
                'is_sent' : False,
            }
            obj = Needs(**insert_dict)
            session.add(obj)
        session.commit()
        if break_counter > 3 :
            break
