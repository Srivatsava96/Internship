# -----------------------------------------------------------------------------
# Description: Script to import icd9 code from file into mongoDB
# Author: Srivatsava
# Date: 27-06-2017
#------------------------------------------------------------------------------

import os
import sys
import getopt

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
    sys.path.append(proj_path)

from Source.modelCdIcd9 import icd_codes9
from Source.cntCdApp import CdApp

logger = CdApp.getLogger()

def get_dataPath():
    dataDir = CdApp.getAppConfig().get('DataDir')
    if not dataDir:
        raise ImportError('Config file error, DataDir not defined')
    
    dataFile = CdApp.getAppConfig().get('icd9DataFile')
    if not dataFile:
        raise ImportError('Config file error, DataFile not defined')
    
    dataPath = os.path.join(dataDir, dataFile)
    return dataPath
#------------------------------------------------------------------------------

def import_data(dataPath, clean_import, delete_col):
    if (delete_col == True):
        icd_codes9.drop_collection()
        return
    
    with open(dataPath) as f:
        for line in f:
            dbIcd = None
            word = line[:5].strip()
            
            if clean_import:
                dbIcd = icd_codes9.objects(code=word).first()
            
            if dbIcd:
                dbIcd.updateUsingDict(line)
                logger.info('is the time of update of the icd %s to icd-9.',
                             word)
                dbIcd.save()
            
            else:
                ndbIcd = icd_codes9()
                ndbIcd.updateUsingDict(line)
                logger.info('is the time of insert of the icd %s to icd-9.',
                             word)
                ndbIcd.save()
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
