# -----------------------------------------------------------------------------
# Description: Script to import patient data from csv file into mongoDB
# Author: Srivatsava
# Date: 08-08-2017
#------------------------------------------------------------------------------


import csv
import pymongo
import os

#connection = pymongo.MongoClient('localhost',27017)
cur_path = os.path.dirname(__file__)
new_path = os.path.relpath('..\\Data\\FakeNameGenerator.com_3c6159aa.csv',cur_path)
f = open(new_path, encoding='utf_8')
reader = csv.reader(f)
for row in reader:
    print (row)
f.close()