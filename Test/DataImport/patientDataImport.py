# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 08-08-2017
#------------------------------------------------------------------------------

import csv
import pymongo
import os
import patient

connection = pymongo.MongoClient('localhost',27017)
db = connection.mydb
data = db.patients
cur_path = os.path.dirname(__file__)
# TODO: Why do you need relative path?

new_path = os.path.relpath('..\\Data\\FakeNameGenerator.com_3c6159aa.csv',cur_path)
with open(new_path, encoding='utf_8') as f:
	reader = csv.DictReader(f)
	i=0;
	for row in reader:
		i += 1
		patient_obj = patient.Patient(i,row['Gender'],row['Title'],row['GivenName'],row['MiddleInitial'],row['Surname'],row['StreetAddress'],row['City'],row['State'],row['ZipCode'],row['Birthday'])
		data.insert_one(patient_obj.loadOneFile())
f.close()