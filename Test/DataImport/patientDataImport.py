# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 08-08-2017
#------------------------------------------------------------------------------

import csv
import pymongo
import os
from Source.CdPatient import patient
from Source.CdApp import CdApp

#1. Connect to Database
CdApp.connectDb()

#2. Get patient data file
dataDir = CdApp.getAppConfig().get('DataDir')
if not dataDir:
	raise ImportError('Config file error, DataDir not defined')

dataFile = CdApp.getAppConfig().get('DataFile')
if not dataFile:
	raise ImportError('Config file error, DataFile not defined')

dataPath = os.path.join(dataDir, dataFile)

#3. parser and save in database
with open(dataPath, encoding='utf_8') as csvFile:
	reader = csv.DictReader(csvFile)

	for count, patDict in enumerate(reader):
		#Post.objects.first()
		dbPatient = patient.objects(nationalID=patDict['NationalID']).first()
		if dbPatient:
			print("Patient exist in database")
			dbPatient.updateUsingDict(patDict=patDict)
		else:
			print("Adding new patient in database")
			dbPatient = patient()
			dbPatient.updateUsingDict(patDict=patDict)
		dbPatient.save()
			
			
		
		
		
		

"""
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
"""