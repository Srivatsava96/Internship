# -----------------------------------------------------------------------------
# Description: Controller for lookup of Physician search
# Author: Srivatsava
# Date: 30-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

from cntCdApp import CdApp

logger = CdApp.getLogger()

@bottle.route('/')
def home_page():
    return bottle.template('viewPhysicianLookup.tpl')
#------------------------------------------------------------------------------

@bottle.route('/physician_lookup_org', method='POST')
def search():
    try:
        client = pymongo.MongoClient("mongodb://localhost")
        db = client.ClinicalData
        collection = db.physician
        lastname = request.forms.get('lne', default='')
        firstname = request.forms.get('first_name',default='')
        npi = request.forms.get('npi',default=None)
        typep = request.forms.get('type')
        if(typep == 'NPI'):
            result = collection.find_one({'NPI':npi})
            if (result == None):
                return "No record found with given NPI"
            else:
                if (result['n1']=='1'):
                    return bottle.template('viewNpi.tpl',phy = result)
                else:
                    return bottle.template()
            
        else:
            if firstname == None:
                firstname=""
            
            if firstname and lastname:
                str1 = '.*'
                firstname = str1 + firstname + str1
                lastname = str1 + lastname + str1
                result = collection.find({'$and':[{'n5':{'$regex':lastname}},
                                                  {'n6':{'$regex':firstname}}]})
            elif lastname:
                result = collection.find({'n5':lastname})
                
            return bottle.template('viewPhysicianFL.tpl',rows = result)
    except Exception as e:
        logger.error("ERROR: {}".format(e))
#------------------------------------------------------------------------------

@bottle.route('/ajax')
def get_speciality():
    try:
        client = pymongo.MongoClient("mongodb://localhost")
        db = client.ClinicalData
        collection = db.physician
        result = collection.find_one({},{'_id':0,'NPI':1})
        return result
    except Exception as e:
        logger.error("ERROR: {}".format(e))
#------------------------------------------------------------------------------
    
@bottle.route('/physician_lookup_pat', method = "POST")
def pat_search():
    try:
        client = pymongo.MongoClient("mongodb://localhost")
        db = client.ClinicalData
        collection = db.physician
        lastname = request.forms.get('lne', default='')
        firstname = request.forms.get('first_name',default='')
        zipcode = request.forms.get('zip',default ='')
        speciality =request.forms.get('speciality',default = '')
        state = request.forms.get('state',default='')
        str1 = '.*'
        lastname = str1 + lastname + str1
        firstname = str1 + firstname + str1
        zipcode = str1 + zipcode + str1
        speciality = str1 + speciality + str1
        state = str1 + state + str1
        result = collection.find({'$and':[{'n5':{'$regex':lastname}},
                                          {'n6':{'$regex':firstname}},
                                          ]})
        return bottle.template('viewPhysicianFL.tpl',rows = result)
    except Exception as e:
        logger.error("ERROR: {}".format(e))

@bottle.route('/list')
def list_me():
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.ClinicalData
    collection = db.states
    return collection.find()

bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------