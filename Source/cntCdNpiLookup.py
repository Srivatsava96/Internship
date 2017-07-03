# -----------------------------------------------------------------------------
# Description: Controller for lookup of NPI data
# Author: Srivatsava
# Date: 26-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

from Source.cntCdApp import CdApp

logger = CdApp.getLogger()

@bottle.route('/')
def home_page():
    return bottle.template('viewNpiLookup.tpl')
#------------------------------------------------------------------------------

@bottle.route('/npi_lookup', method='POST')
def search():
    try:
        client = pymongo.MongoClient("mongodb://localhost")
        db = client.ClinicalData
        collection = db.physician
        lastname = request.forms.get('lne', default=None)
        firstname = request.forms.get('firstname',default=None)
        npi = request.forms.get('npi')
        if(npi!=None):
            result = collection.find_one({'NPI':npi})
            if (result == None):
                return "No record found with given NPI"
            else:
                return bottle.template('viewNpi.tpl',phy = result)
            
        else:
            result = collection.find({'$and':[{'Provider_Last_Name':{'$regex':lastname}},
                                              {'Provider_First_Name':{'$regex':firstname}}]})
            return bottle.template()
    except Exception as e:
        logger.error("ERROR: {}".format(e))
#------------------------------------------------------------------------------


    
bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------