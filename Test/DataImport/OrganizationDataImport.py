# -----------------------------------------------------------------------------
# Description: Script to import organization data from json file into mongoDB
# Author: Srivatsava
# Date: 26-05-2017
#------------------------------------------------------------------------------

import os
import json
import sys

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
	sys.path.append(proj_path)

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
logger = CdApp.getLogger()

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