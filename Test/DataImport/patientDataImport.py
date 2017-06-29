# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 20-05-2017
#------------------------------------------------------------------------------

import csv
import os
import sys
import logging

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
	sys.path.append(proj_path)

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
logger = CdApp.getLogger()

#3. parser and save in database
with open(dataPath, encoding='utf_8') as csvFile:
	reader = csv.DictReader(csvFile)

	for count, patDict in enumerate(reader):
		#Post.objects.first()
		dbPatient = patient.objects(nationalID=patDict['NationalID']).first()
		if dbPatient:
			print("Patient exist in database")
			dbPatient.updateUsingDict(patDict=patDict)
			logger.info('is the time of update of the patient %s to patient.',
                         patDict['NationalID'])
		else:
			print("Adding new patient in database")
			dbPatient = patient()
			dbPatient.updateUsingDict(patDict=patDict)
			logger.info('is the time of insert of the patient %s to patient.',
                         patDict['NationalID'])
		dbPatient.save()
#------------------------------------------------------------------------------