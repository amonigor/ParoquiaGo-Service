import requests
import json
import os
from api.geocodingapi import Geocoding

class Address:
    def __init__(self):
        self.base_url = os.environ.get('DIOCESE_API_URL')

    def extract_address(self, text):
        text = text.strip()
        text = text.replace('\\', '')
        text = text.replace('Endereço:', 'Endereco:')
        text = text.replace('Enderaço:', 'Endereco:')
        text = text.replace('Enderaco:', 'Endereco:')
        text = text.replace('<strong>', '')
        text = text.replace('</strong>', '')
        text = text.replace('&nbsp;', '')
        text = text.replace('( <a', '&&&')
        text = text.replace('(<a', '&&&')
        text = text.replace('<br', '&&&')
        text = text.replace('</p', '&&&')
        start = text.find('Endereco:') + 9
        end = text.find('&&&', start)
        return text[start:end].strip()

    def get_church_list(self):
        response = requests.get(self.base_url + "/api/index.php/v1/mini/paroquias")
        churches = json.loads(response.content)
        return churches['data']

    def get_data(self):
        geocoding = Geocoding()

        return [geocoding.get_location(), self.base_url]

        churches = self.get_church_list()
        data = {
            "count": 0,
            "data": []
        }

        for church in churches:
            if (church['state'] != 2): 
                address = self.extract_address(church['fulltext'] if church['fulltext'] else church['introtext'])
                data['data'].append(
                    {
                        "id": church['id'],
                        "address": address,
                        "coordinates": geocoding.get_location(address),
                        "name": church['title'],
                        "images": json.loads(church['images'])
                    }
                )

        data['count'] = len(data['data'])
        return json.dumps(data, indent=4)