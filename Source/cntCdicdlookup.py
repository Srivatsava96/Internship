# -----------------------------------------------------------------------------
# Description: Controller for icd10 code lookup
# Author: Srivatsava
# Date: 27-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

@bottle.route('/')
def home_page():
    return bottle.template('viewicdlookup.tpl')
#------------------------------------------------------------------------------

@bottle.route('/icd_lookup', method = "POST")
def icd_search():
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.ClinicalData
    collection = db.icd_codes
    icd = request.forms.get('icd', default=None)
    disease = request.forms.get('disease',default=None)
    if (icd!=''):
        result = collection.find_one({'code':icd})
        if(result!=None):
            return bottle.template('viewicd.tpl',icd=result)
        else:
            return "No code found in database"
    
    elif(disease!=''):
        str1 = ".*"
        disease = str1+disease+str1
        result = collection.find({'disease':{'$regex':disease}})
        if(result!=None):
            return bottle.template('viewdisease10.tpl',icd=result)
        else:
            return "No match found in database"
        
    else:
        return "No ICD code entered"
#------------------------------------------------------------------------------
    
bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------