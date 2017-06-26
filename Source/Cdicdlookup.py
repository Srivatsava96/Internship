import bottle
import pymongo
from bottle import request

@bottle.route('/')
def home_page():
    return bottle.template('icdlookup.tpl')

@bottle.route('/icd_lookup', method = "POST")
def icd_search():
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.ClinicalData
    collection = db.icd_codes
    icd = request.forms.get('icd', default=None)
    if (icd!=None):
        result = collection.find_one({'code':icd})
        if(result!=None):
            return bottle.template('Viewicd.tpl',icd=result)
        else:
            return "No code found in database"
    else:
        return "No ICD code entered"
    
bottle.debug(True)
bottle.run(host='localhost',port=8082)