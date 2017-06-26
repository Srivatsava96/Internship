# -----------------------------------------------------------------------------
# Description: Script to import physician data from csv file into mongoDB
# Author: Srivatsava
# Date: 08-08-2017
#------------------------------------------------------------------------------


import csv
import pymongo
import os
from Source.CdApp import CdApp
from Source.CdPhysician import Physician

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

#3. parser and save in database
#with open(dataPath, encoding='utf_8') as csvFile:
#	reader = csv.DictReader(csvFile)

with open(dataPath, encoding='utf_8') as infile:
	for line in infile:
		Phydict = line.split(',')
		Phydict = [p.strip('" ') for p in Phydict ]
		# 1. Find if the physician exist in DB
		dbPhy = Physician.objects(NPI=Phydict[0]).first()
		
		# 2. if exist use the same physician to update
		if dbPhy:
			print("Updating existing database")
			dbPhy.UpdateUsingDict(Phydict = Phydict)
			dbPhy.save()
		else:	
			# 3. if not, create new physician and update
			print("Adding new physician in database")
			ndbPhy = Physician()
			ndbPhy.UpdateUsingDict(Phydict = Phydict)
			ndbPhy.save()