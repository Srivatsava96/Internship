# -----------------------------------------------------------------------------
# Description: Script to import organization data from json file into mongoDB
# Author: Srivatsava
# Date: 26-05-2017
#------------------------------------------------------------------------------

import os
import json

from Source.modelCdOrganization import Organisation
from Source.cntCdApp import CdApp


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
js = open(dataPath)
OrgDict=json.load(js)

dbOrg = Organisation.objects(npi=OrgDict['NPI']).first()
if dbOrg:
	print("Organization exist in database")
	dbOrg.UpdateUsingDict(OrgDict = OrgDict)
else:
	print("Adding new organization in database")
	dbOrg = Organisation()
	dbOrg.UpdateUsingDict(OrgDict = OrgDict)
dbOrg.save()
#------------------------------------------------------------------------------