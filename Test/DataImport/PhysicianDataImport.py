# -----------------------------------------------------------------------------
# Description: Script to import physician data from csv file into mongoDB
# Author: Srivatsava
# Date: 26-06-2017
#------------------------------------------------------------------------------


import os
import sys
import csv
from getopt import getopt
#from Test.DataImport.icd10DataImport import dataPath

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
	sys.path.append(proj_path)

from Source.cntCdApp import CdApp
from Source.modelCdPhysician import Physician

logger = CdApp.getLogger()

def get_dataPath():
	
	#2. Get npi data file
	dataDir = CdApp.getAppConfig().get('DataDir')
	if not dataDir:
		raise ImportError('Config file error, DataDir not defined')
	
	dataFile = CdApp.getAppConfig().get('PhyDataFile')
	if not dataFile:
		raise ImportError('Config file error, DataFile not defined')
	
	dataPath = os.path.join(dataDir, dataFile)
	return dataPath
#------------------------------------------------------------------------------

def import_data(data_path, clean_import, delete_col):
	if (delete_col == True):
		Physician.drop_collection()
		return
	with open(data_path, encoding='utf_8') as infile:
		reader = csv.reader(infile)
		for count,Phydict in enumerate(reader):
			dbPhy = None
			
			if not count%2000:
				print('{}'.format(count))
			
			if len(Phydict)!=329:
				print('{}'.format(len(Phydict)))
					
			if not clean_import:
				dbPhy = Physician.objects(NPI=Phydict[0]).first()
				
			if dbPhy:
				# 2. if exist use the same physician to update
				dbPhy.UpdateUsingDict(Phydict = Phydict)
				logger.info('is the time of update of the phy %s to database',
	                         Phydict[0])
				dbPhy.save()
			else:	
				# 3. if not, create new physician and update
				ndbPhy = Physician()
				ndbPhy.UpdateUsingDict(Phydict = Phydict)
				logger.info('is the time of insert of the phy %s to database',
	                         Phydict[0])
				ndbPhy.save()
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
