import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime

class News:
    def __init__(self):
        load_dotenv()
        self.news_url = os.getenv('NEWS_URL')

    def get_news(self):
        headers = {'x-requested-with':'root_URL_Of_Endpoint', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        response = requests.get(self.news_url, headers=headers)
        soup = BeautifulSoup(response.content, features='html.parser')

        tableRows = soup.find_all('tr', {'class': 'cat-list-row0'})

        data = {
            "count": 0,
            "data": []
        }

        for row in tableRows:
            newRow = list(filter(lambda content: content != '\n', row.contents))
            data['data'].append({
                'link': self.news_url + '/' + newRow[0].find('a', href=True)['href'].replace('/noticias/presenca-diocesana/noticias/', ''),
                'title': newRow[0].find('a').get_text().replace('\n', '').replace('\t', ''),
                'date': datetime.strptime(newRow[1].get_text().replace('\n', '').replace('\t', ''), '%d-%m-%Y').isoformat()
            })
        
        data['count'] = len(data['data'])

        return json.dumps(data, indent=4)