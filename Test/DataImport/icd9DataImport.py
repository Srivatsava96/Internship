# -----------------------------------------------------------------------------
# Description: Script to import icd9 code from file into mongoDB
# Author: Srivatsava
# Date: 27-06-2017
#------------------------------------------------------------------------------

import os
import sys
import logging

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
proj_path = os.path.dirname(proj_path)
if proj_path not in sys.path:
    sys.path.append(proj_path)

from Source.modelCdIcd9 import icd_codes9
from Source.cntCdApp import CdApp

#1. Connect to Database
CdApp.connectDb()

#2. Get patient data file
dataDir = CdApp.getAppConfig().get('DataDir')
if not dataDir:
    raise ImportError('Config file error, DataDir not defined')

dataFile = CdApp.getAppConfig().get('icd9DataFile')
if not dataFile:
    raise ImportError('Config file error, DataFile not defined')

dataPath = os.path.join(dataDir, dataFile)
logger = CdApp.getLogger()

#3. parser and save in database
with open(dataPath) as f:
    for line in f:
        word = line[:5].strip()
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