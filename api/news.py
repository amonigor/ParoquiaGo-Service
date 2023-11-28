import json
import time
import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

class News:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('NEWS_URL')
        self.token = os.getenv('GITHUB_TOKEN')

    def get_data(self):
        # INICIALIZA O NAVEGADOR
        options = Options()
        options.add_argument('-headless')
        os.environ['GH_TOKEN'] = self.token
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(options=options, service=service)
        driver.maximize_window()
        driver.get(self.url)

        # COMEÇA A RASPAGEM
        cookiesButton = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'pjAcceptCookieBarBtn')))
        cookiesButton.click()

        limit = driver.find_element(By.CSS_SELECTOR, '#limit')
        limitOption = driver.find_element(By.CSS_SELECTOR, '#limit > option:nth-child(9)')
        limit.click()
        limitOption.click()

        time.sleep(1)

        news = driver.find_elements(By.CSS_SELECTOR, '.list-title > a')
        dates = driver.find_elements(By.CSS_SELECTOR, '.list-date')
        newsList = []

        for i, new in enumerate(news):
            header = str(new.get_attribute('innerHTML'))
            header = header.replace('\t', '')
            header = header.replace('\n', '')
            
            date = str(dates[i].get_attribute('innerHTML'))
            date = date.replace('\t', '')
            date = date.replace('\n', '')
            date = date.replace('-', '/')

            newsList.append({
                'header': header,
                'link': new.get_attribute('href'),
                'date': date,
            })

        data = {
            'count': len(newsList),
            'data': newsList,
        }

        driver.quit()
        return json.dumps(data, indent=4)
