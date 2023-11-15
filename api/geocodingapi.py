import requests
import json
import os

class Geocoding:
    def __init__(self):
        self.key = os.environ.get('GOOGLE_MAPS_API_KEY')
        self.url = os.environ.get('GEOCODING_URL')

    def get_location(self, address):
        return [self.key, self.url]
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
