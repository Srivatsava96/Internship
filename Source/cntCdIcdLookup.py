# -----------------------------------------------------------------------------
# Description: Controller for icd10 code lookup
# Author: Srivatsava
# Date: 27-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

from cntCdApp import CdApp

logger = CdApp.getLogger()

@bottle.route('/')
def home_page():
    try:
        return bottle.template('viewIcdLookup.tpl')
    except Exception as e:
        logger.error("ERROR: {}".format(e))
#------------------------------------------------------------------------------

@bottle.route('/icd_lookup', method = "POST")
def icd_search():
    try:
        client = pymongo.MongoClient("mongodb://localhost")
        db = client.ClinicalData
        collection = db.icd_codes
        icd = request.forms.get('icd', default=None)
        disease = request.forms.get('disease',default=None)
        if (icd!=''):
            result = collection.find_one({'code':icd})
            if(result!=None):
                return bottle.template('viewIcd.tpl',icd=result)
            else:
                return "No code found in database"
        
        elif(disease!=''):
            str1 = ".*"
            disease = str1+disease+str1
            result = collection.find({'disease':{'$regex':disease}})
            if(result!=None):
                return bottle.template('viewDisease10.tpl',icd=result)
            else:
                return "No match found in database"
            
        else:
            return "No ICD code entered"
    except Exception as e:
        logger.error("ERROR: {}".format(e))
#------------------------------------------------------------------------------
    
bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------