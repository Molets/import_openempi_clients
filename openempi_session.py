import requests

class Openempi_session:
    def __init__(self):
        self.findPersonsByAttributesURL = "http://192.168.0.125:8080/openempi-admin/openempi-ws-rest/person-query-resource/findPersonsByAttributes"
        self.key_url = "http://192.168.0.125:8080/openempi-admin/openempi-ws-rest/security-resource/authenticate"
        self.key_body = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><authenticationRequest><password>h9/L_Dr,^-$m4ST:</password><username>admin</username></authenticationRequest>"
    
    def get_key(self):
        response = requests.put(self.key_url, self.key_body, headers={'Content-Type': 'application/xml'})
        key = response.text
        return key