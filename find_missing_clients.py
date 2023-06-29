from openempi_session import Openempi_session
from helper import get_patients_from_csv
from helper import write_data_to_csv

def main():
    filename = input("Enter CSV file name: ")
    openempi_session = Openempi_session()
    patients = get_patients_from_csv(filename)
    found_patients = []
    missing_patients = []
    for patient in patients:
        if(patient.is_patient_in_openempi(openempi_session)):
            found_patients.append(patient)
        else:
            missing_patients.append(patient)
        
    print("=================Found Patients=================\n")
    for patient in found_patients:
        print(patient.givenName+" "+patient.familyName+"\n")

    print("=================Missing Patients=================\n")
    for patient in missing_patients:
        print(patient.givenName+" "+patient.familyName+"\n")

    write_data_to_csv("found_patients.csv", found_patients)
    write_data_to_csv("missing_patients.csv", missing_patients)



main()