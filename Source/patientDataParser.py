# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 08-08-2017
#------------------------------------------------------------------------------


import csv
import pymongo

#connection = pymongo.MongoClient('localhost',27017)
f = open('FakeNameGenerator.com_3c6159aa.csv', encoding='utf_8')
reader = csv.reader(f)
for row in reader:
    print (row)
f.close()