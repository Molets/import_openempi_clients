import csv
from patient import Patient
from patient import personIdentifier

def get_patients_from_csv(file):
    patients = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None) #Skip header
        for row in csv_reader:
            patientID = personIdentifier(row[0])
            patient = Patient(patientID, row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[9], row[10], row[12], row[13])
            patients.append(patient)
        return patients
    
 
def write_data_to_csv(filename, patient_array):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        header = ["identifier","givenname","familyname","address1","address2","city","dateOfBirth","phoneNumber","identifier","gender","mothersMaidenName","familyname2","motherName","maritalstatusCode"]
        writer.writerow(header)
        for patient in patient_array:
            writer.writerow([patient.personIdentifier.id, patient.givenName, patient.familyName, patient.address1, patient.address2, patient.city,patient.dateOfBirth,patient.phoneNumber,'',patient.gender, patient.mothersMaidenName,'',patient.motherName, patient.maritalstatusCode])
