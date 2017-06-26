import bottle
import pymongo
from bottle import request

@bottle.route('/')
def home_page():
    return bottle.template('npilookup.tpl')

@bottle.route('/npi_lookup', method='POST')
def search():
    client = pymongo.MongoClient("mongodb://localhost")
    db = client.ClinicalData
    collection = db.physician
    lastname = request.forms.get('lne', default=None)
    firstname = request.forms.get('firstname',default=None)
    npi = request.forms.get('npi')
    print(npi)
    if(npi!=None):
        result = collection.find_one({'NPI':npi})
        print(result)
        if (result == None):
            return "No record found with given NPI"
        return bottle.template('Viewnpi.tpl',phy = result)
    else:
        result = collection.find({'$and':[{'Provider_Last_Name':lastname},{'Provider_First_Name':firstname}]})
        return bottle.template()
    
bottle.debug(True)
bottle.run(host='localhost',port=8082)