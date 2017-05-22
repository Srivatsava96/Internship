import os
import json
from Source.CdOrganization import Organisation_test
from Source.CdApp import CdApp



#1. Connect to Database
CdApp.connectDb()

#2. Get patient data file
dataDir = CdApp.getAppConfig().get('Org_DataDir')
if not dataDir:
	raise ImportError('Config file error, DataDir not defined')

dataFile = CdApp.getAppConfig().get('Org_DataFile')
if not dataFile:
	raise ImportError('Config file error, DataFile not defined')

dataPath = os.path.join(dataDir, dataFile)
"""
dataDir = "D:/Project/Internship/Data"
dataFile = "Organization_HospitalA.json"
datapath = os.path.join(dataDir,dataFile)
"""
js = open(dataPath)
OrgDict=json.load(js)

dbOrg = Organisation_test.objects(npi=OrgDict['NPI']).first()
if dbOrg:
	print("Organization exist in database")
	dbOrg.UpdateUsingDict(OrgDict = OrgDict)
else:
	print("Adding new organization in database")
	dbOrg = Organisation_test()
	dbOrg.UpdateUsingDict(OrgDict = OrgDict)
dbOrg.save()