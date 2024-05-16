select distinct a.identifier,c.given_name as givenName,c.family_name as familyName,pa.city_village as address1,pa.address2,pa.state_province as city,pn.birthdate as dateOfBirth
,pc.value as phoneNumber,ni.identifier as nationalID,pn.gender,c.middle_name as mothersMaidenName,c.family_name2,ts.value as motherName,msc.value as maritalStatusCode
from 
(select distinct patient_id,identifier,date_created from patient_identifier where identifier_type=3 and patient_id not in 
(select distinct patient_id from patient_identifier where identifier_type=5)) as a join
(select distinct person_id,obs_datetime from obs where obs_datetime between  date_sub(now(), interval 3 day) and now() and concept_id=2165 and voided=0) as b 
on a.patient_id=b.person_id left outer join (select distinct person_id,given_name,family_name,middle_name,family_name2 from person_name ) as c on a.patient_id=c.person_id left outer join
(select person_id,gender,birthdate from person ) as pn on a.patient_id=pn.person_id left outer join
(select person_id, address2,city_village,state_province,postal_code from person_address) as pa on a.patient_id=pa.person_id left outer join
(select person_id,person_attribute_id,value from person_attribute where person_attribute_type_id=26) as pc on a.patient_id=pc.person_id left outer join
(select patient_id,identifier,identifier_type from patient_identifier where identifier_type=4) as ni on a.patient_id = ni.patient_id left outer join
(select person_id,person_attribute_id,value from person_attribute where person_attribute_type_id =17) as ts on a.patient_id = ts.person_id left outer join
(select person_id,person_attribute_id,value from person_attribute where person_attribute_type_id =28) as msc on a.patient_id= msc.person_id
INTO OUTFILE '/var/lib/mysql-files/HTS_EXPORT.csv'  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
 LINES TERMINATED BY '\n';

