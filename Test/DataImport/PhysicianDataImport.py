# -----------------------------------------------------------------------------
# Description: Script to import physician data from csv file into mongoDB
# Author: Srivatsava
# Date: 26-06-2017
#------------------------------------------------------------------------------


import os

from Source.cntCdApp import CdApp
from Source.modelCdPhysician import Physician

#1. Connect to Database
CdApp.connectDb()

#2. Get patient data file
dataDir = CdApp.getAppConfig().get('DataDir')
if not dataDir:
	raise ImportError('Config file error, DataDir not defined')

dataFile = CdApp.getAppConfig().get('PhyDataFile')
if not dataFile:
	raise ImportError('Config file error, DataFile not defined')

dataPath = os.path.join(dataDir, dataFile)

#3. parse and save in database
with open(dataPath, encoding='utf_8') as infile:
	for line in infile:
		Phydict = line.split(',')
		Phydict = [p.strip('" ') for p in Phydict ]
		dbPhy = Physician.objects(NPI=Phydict[0]).first()
		# 1. Find if the physician exist in DB
		if dbPhy:
			# 2. if exist use the same physician to update
			dbPhy.UpdateUsingDict(Phydict = Phydict)
			dbPhy.save()
		else:	
			# 3. if not, create new physician and update
			ndbPhy = Physician()
			ndbPhy.UpdateUsingDict(Phydict = Phydict)
			ndbPhy.save()
#------------------------------------------------------------------------------