import requests
import xml.etree.ElementTree as ET

class Patient:
    def __init__(self, givenName, familyName, dateCreated, date, obs_id):
        identifier,,,,,,,,,,,,,
        self.givenName = givenName
        self.familyName = familyName
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber
        self.phoneNumber = phoneNumber
        self.mothersMaidenName = mothersMaidenName
        self.familyname2 = familyname2
        self.motherName = motherName
        self.maritalstatusCode = maritalstatusCode
        self.gender = gender
        self.date = date
        self.obs_id = obs_id

    def convert_to_xml(self):
        xml_patient = "<person><givenName>"+self.givenName+"</givenName><familyName>"+self.familyName+"</familyName><dateCreated>"+self.dateCreated+"</dateCreated></person>"
        return xml_patient
    
    def is_patient_in_openempi(self, openempi_session):
        api_url = openempi_session.findPersonsByAttributesURL
        headers = {'Content-Type': 'application/xml', 'OPENEMPI_SESSION_KEY': openempi_session.get_key()}
        patient_in_xml = self.convert_to_xml()
        response = requests.post(api_url, patient_in_xml, headers=headers)
        if(response.status_code == 200):
            response_xml = ET.fromstring(response.text)
            response_len = len(response_xml)
            if(response_len <= 0):
                return False
            else:
                return True
        else:
            print("Print failed to validate patient error code: ")
            print(response.status_code)
            return False

    def create_patient_on_empi(self, openempi_session):
        print("send patient")