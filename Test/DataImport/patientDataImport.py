# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 20-05-2017
#------------------------------------------------------------------------------

import csv
import os

from Source.modelCdPatient import patient
from Source.cntCdApp import CdApp

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
#------------------------------------------------------------------------------