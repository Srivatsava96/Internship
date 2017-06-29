# -----------------------------------------------------------------------------
# Description: Controller for lookup of NPI data
# Author: Srivatsava
# Date: 26-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

@bottle.route('/')
def home_page():
    return bottle.template('viewNpiLookup.tpl')
#------------------------------------------------------------------------------

@bottle.route('/npi_lookup', method='POST')
def search():
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
        result = collection.find({'$and':[{'Provider_Last_Name':lastname},
                                          {'Provider_First_Name':firstname}]})
        return bottle.template()
    
bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------