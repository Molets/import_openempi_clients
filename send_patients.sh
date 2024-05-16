#! /bin/bash

docker exec bahmni_docker_emr-service_1 rm -rf /var/lib/mysql-files/HTS_EXPORT.csv

cd $HOME/openmrs-openempi-utilities
#cd $HOME/Documents/Icap/Scrips/HIE docs/openmrs-openempi-utilities

docker exec bahmni_docker_emr-service_1 /usr/bin/mysql -uroot -pP@ssw0rd openmrs -e "source HTS_Export.sql"

docker cp bahmni_docker_emr-service_1:/var/lib/mysql-files/HTS_EXPORT.csv .

python3 demograhics.py

python3 prepare_data.py

python3 find_missing_clients.py

python3 send_missing_clients.py


