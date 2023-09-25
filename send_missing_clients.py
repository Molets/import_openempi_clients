from openempi_session import Openempi_session
from helper import get_patients_from_csv
from helper import write_data_to_csv

def main():
    filename = input("Enter CSV file name: ")
    openempi_session = Openempi_session()
    patients = get_patients_from_csv(filename)
    sent_patients = []
    failed_patients = []
    for patient in patients:
        if(patient.send_to_openempi(openempi_session)):
            sent_patients.append(patient)
        else:
            failed_patients.append(patient)
        
    print("=================Sent Patients=================\n")
    for patient in sent_patients:
        print(patient.givenName+" "+patient.familyName+"\n")

    print("=================Failed Patients=================\n")
    for patient in failed_patients:
        print(patient.givenName+" "+patient.familyName+"\n")

    write_data_to_csv("sent_patients.csv", sent_patients)
    write_data_to_csv("failed_patients.csv", failed_patients)



main()