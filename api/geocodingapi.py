import requests
import json
import os
from dotenv import load_dotenv

class Geocoding:
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.url = os.getenv('GEOCODING_URL')

    def get_location(self, address):
        res = requests.get(
            self.url,
            {
                'address': address,
                'key': self.key,
                'language': 'pt-BR'
            }
        )
        parsedRes = json.loads(res.content)
        return parsedRes['results'][0]['geometry']['location'] if parsedRes['status'] == 'OK' else { 'lat': None, 'lng': None }
