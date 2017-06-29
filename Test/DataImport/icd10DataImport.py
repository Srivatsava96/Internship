# -----------------------------------------------------------------------------
# Description: Script to import icd-10 codes from file into mongoDB
# Author: Srivatsava
# Date: 26-06-2017
#------------------------------------------------------------------------------

import os
import sys

#add source path to sys path
proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
    sys.path.append(proj_path)

from Source.modelCdIcd10 import icd_codes as icdc
from Source.cntCdApp import CdApp

#1. Connect to Database
CdApp.connectDb()

#2. Get patient data file
dataDir = CdApp.getAppConfig().get('DataDir')
if not dataDir:
    raise ImportError('Config file error, DataDir not defined')

dataFile = CdApp.getAppConfig().get('icdDataFile')
if not dataFile:
    raise ImportError('Config file error, DataFile not defined')

dataPath = os.path.join(dataDir, dataFile)
logger = CdApp.getLogger()

#3. parse and save in database
with open(dataPath, encoding='utf_8') as f:
    for line in f:
        word = line[:7].strip()
        dbIcd = icdc.objects(code=word).first()
        if dbIcd:
            dbIcd.updateUsingDict(line)

            logger.info('is the time of update of the icd %s to icd-10.',
                         word)
            dbIcd.save()
        else:
            ndbIcd = icdc()
            ndbIcd.updateUsingDict(line)
            logger.info('is the time of update of the icd %s to icd-10.',
                         word)
            ndbIcd.save()
#------------------------------------------------------------------------------