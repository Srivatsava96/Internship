# -----------------------------------------------------------------------------
# Description: Script to import organization data from json file into mongoDB
# Author: Srivatsava
# Date: 26-05-2017
#------------------------------------------------------------------------------

import os
import json
import sys
import getopt

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
	sys.path.append(proj_path)

from Source.modelCdOrganization import Organisation
from Source.cntCdApp import CdApp

logger = CdApp.getLogger()

def get_dataPath():
	dataDir = CdApp.getAppConfig().get('Org_DataDir')
	if not dataDir:
		raise ImportError('Config file error, DataDir not defined')
	
	dataFile = CdApp.getAppConfig().get('Org_DataFile')
	if not dataFile:
		raise ImportError('Config file error, DataFile not defined')
	
	dataPath = os.path.join(dataDir, dataFile)
	return dataPath
#------------------------------------------------------------------------------

def import_data(dataPath, clean_import, delete_col):
	if (delete_col == True):
		Organisation.drop_collection()
		return
	js = open(dataPath)
	OrgDict=json.load(js)
	dbOrg = None
	if clean_import:
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

def main(argv):
    try:
        opts, args = getopt(argv,"hi:crn",["help="])
        
    except getopt.GetoptError:
        print("PhysicianDataImport.py -i <inputfile> -c <cleanimport>")
        print("-h <help> -r <dropdatabase> -n <normalimport>")
        sys.exit(2)
    
    data_path = None
    clean_import = False
    delete_col = False
    CdApp.connectDb()
    data_path = get_dataPath()
    for opt, arg in opts:
        if opt == '-h':
            print("-c <cleanimport>, -r <dropdatabase>, -i <filepath>")
            sys.exit()
        elif opt in ("-i", "--filepath"):
            data_path = arg
        elif opt in ("-c", "--cleanimport"):
            clean_import = True
        elif opt in ("-r", "--dropdatabase"):
            delete_col = True
        elif opt in ("-n"):
            print("Starting Import")


    import_data(data_path, clean_import, delete_col)
    print('Import done')

if __name__ == "__main__":
    main(sys.argv[1:])                    
#------------------------------------------------------------------------------
