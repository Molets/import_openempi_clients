import requests

class Openempi_session:
    def __init__(self):
        self.isIdentifierinXDSURL = "http://102.37.107.213:8080/api/v1.0/personidentifier/"
        
    def get_key(self):
        response = requests.put(self.key_url, self.key_body, headers={'Content-Type': 'application/xml'})
        key = response.text
        return key
    
