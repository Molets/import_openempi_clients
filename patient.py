import requests
import xml.etree.ElementTree as ET

class personIdentifier:
    def __init__(self, fullid):
        id = fullid.split("&")
        self.id = fullid
        self.identifier = id[0]
        self.namespaceID = id[1]
        self.universalID = id[2]
        self.universalIDTypeCode = id[3]

    def convert_to_xml(self):
        xml_identifier = "<identifier>"+self.identifier+"</identifier><identifierDomain><namespaceIdentifier>"+self.namespaceID+"</namespaceIdentifier><universalIdentifier>"+self.universalID+"</universalIdentifier><universalIdentifierTypeCode>"+self.universalIDTypeCode+"</universalIdentifierTypeCode></identifierDomain>"
        return xml_identifier

class Patient:
    def __init__(self, personIdentifier, givenName, familyName, address1, address2, city,dateOfBirth,phoneNumber,gender, mothersMaidenName,motherName, maritalstatusCode):
        self.personIdentifier = personIdentifier
        self.givenName = givenName
        self.familyName = familyName
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.dateOfBirth = dateOfBirth
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.mothersMaidenName = mothersMaidenName
        self.motherName = motherName
        self.maritalstatusCode = maritalstatusCode
        
    def convert_to_xml(self):
        xml_patient = "<person><address1>"+self.address1+"</address1><address2>"+self.address2+"</address2><city>"+self.city+"</city><country>Lesotho</country><familyName>"+self.familyName+"</familyName><dateOfBirth>"+self.dateOfBirth+"</dateOfBirth><gender><genderCode>"+self.gender+"</genderCode></gender><givenName>"+self.givenName+"</givenName><maritalStatusCode>"+self.maritalstatusCode+"</maritalStatusCode><motherName>"+self.motherName+"</motherName><mothersMaidenName>"+self.mothersMaidenName+"</mothersMaidenName><personIdentifiers>"+self.personIdentifier.convert_to_xml()+"</personIdentifiers><phoneNumber>"+self.phoneNumber+"</phoneNumber></person>"
        return xml_patient
    
    def search_parameters(self):
        xml_search_parameters = "<personIdentifier>"+self.personIdentifier.convert_to_xml()+"</personIdentifier>"
        return xml_search_parameters
    
    def is_patient_in_openempi(self, openempi_session):
        api_url = openempi_session.findPersonsByIdURL
        headers = {'Content-Type': 'application/xml', 'OPENEMPI_SESSION_KEY': openempi_session.get_key()}
        xml_search_body = self.search_parameters()
        response = requests.post(api_url, xml_search_body, headers=headers)
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
    
    def send_to_openempi(self, openempi_session):
        api_url = openempi_session.importPersonURL
        headers = {'Content-Type': 'application/xml', 'OPENEMPI_SESSION_KEY': openempi_session.get_key()}
        xml_patient = self.convert_to_xml()
        response = requests.put(api_url, xml_patient, headers=headers)
        if(response.status_code == 200):
            return True
        else:
            # print("Print failed to validate patient error code: ")
            print(xml_patient)
            # print(response.status_code)
            return False

    def create_patient_on_empi(self, openempi_session):
        print("send patient")