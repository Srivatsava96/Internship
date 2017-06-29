# -----------------------------------------------------------------------------
# Description: Controller file for mapping icd9 and icd10 codes
# Author: Srivatsava
# Date: 27-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

@bottle.route('/')
def home_page():
    return bottle.template('viewIcdMapping.tpl')
#------------------------------------------------------------------------------

@bottle.route('/icd_map', method="POST")
def icd_map():
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.ClinicalData
    icd9 = request.forms.get('icd9',default=None)
    icd10 = request.forms.get('icd10',default=None)
    if(icd9 != ''):
        collection = db.icd_codes9
        result = collection.find_one({'code':icd9})
        if(result!=None):
            str1 = '.*'
            disease = str1 + result['disease'] + str1
            collection = db.icd_codes
            result2 = collection.find_one({'disease':{'$regex':disease}})
            if(result2!=None):
                return bottle.template('viewIcd10Map.tpl',icd=result2)
            else:
                return "No matching ICD code found by the disease description."
        else:
            return "ICD9 code not available"
    elif(icd10 != ''):
        collection = db.icd_codes
        result = collection.find_one({'code':icd10})
        if(result != None):
            str1 = '.*'
            disease = str1 + result['disease'] + str1
            collection = db.icd_codes9
            result2 = collection.find_one({'disease':{'$regex':disease}})
            if(result2 !=None):
                return bottle.template('viewIcd9Map.tpl',icd=result2)
            else:
                return "No matching ICD code found by the disease description."
        else:
            return "ICD9 code not available"
    else:
        return "No ICD code entered"

bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------