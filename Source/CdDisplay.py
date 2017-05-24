import bottle
import pymongo

@bottle.route('/')
def home_page():
	return bottle.template('hello.tpl')

@bottle.route('/patients')
def patients_page():
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.patient
	result = collection.find()
	return bottle.template('patients.tpl', rows = result)

@bottle.route('/organizations')
def organisation_page():
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.organisation_test
	result = collection.find()
	return bottle.template('Organization.tpl',rows = result)

bottle.debug(True)
bottle.run(host='localhost',port=8082)