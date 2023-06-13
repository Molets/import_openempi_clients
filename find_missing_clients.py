import csv
from patient import Patient
from openempi_session import Openempi_session

def get_patients_from_csv():
    patients = []
    with open('patients.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            name = row[0].split(" ")
            patient = Patient(name[0], name[1], row[3], row[1], row[2])
            patients.append(patient)
        return patients
    
# Write clients to csv file
def write_data_to_csv(filename, patient_array):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for patient in patient_array:
            writer.writerow([patient.givenName+" "+patient.familyName, patient.date, patient.obs_id, patient.dateCreated])

def main():
    openempi_session = Openempi_session()
    patients = get_patients_from_csv()
    found_patients = []
    missing_patients = []
    for patient in patients:
        if(patient.is_patient_in_openempi(openempi_session)):
            found_patients.append(patient)
        else:
            missing_patients.append(patient)
        
    print("=================Found Patients=================\n")
    for patient in found_patients:
        print(patient.givenName+" "+patient.familyName+" "+patient.dateCreated+"\n")

    print("=================Missing Patients=================\n")
    for patient in missing_patients:
        print(patient.givenName+" "+patient.familyName+" "+patient.dateCreated+"\n")

    write_data_to_csv("found_patients.csv", found_patients)
    write_data_to_csv("missing_patients.csv", missing_patients)



main()