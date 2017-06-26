# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 08-08-2017
#------------------------------------------------------------------------------

import pymongo
import os
from Source.CDicd import icd_codes
from Source.CdApp import CdApp

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

#3. parser and save in database
with open(dataPath, encoding='utf_8') as f:
    for line in f:
        word = line[:7].strip()
        dbIcd = icd_codes.objects(code=word).first()
        if dbIcd:
            dbIcd.updateUsingDict(line)
            dbIcd.save()
        else:
            ndbIcd = icd_codes()
            ndbIcd.updateUsingDict(line)
            ndbIcd.save()
#   dbicd = icd_codes()
#   dbicd.updateUsingDict()
#  dbicd.save()