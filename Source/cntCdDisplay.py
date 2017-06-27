# -----------------------------------------------------------------------------
# Description: Controller for lookup of patient and orgnization data
# Author: Srivatsava
# Date: 06-06-2017
#------------------------------------------------------------------------------

import bottle
import pymongo
from bottle import request

@bottle.route('/')
def home_page():
	return bottle.template('viewhello.tpl')
#------------------------------------------------------------------------------

@bottle.route('/patients')
def patients_page():
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.patient
	result = collection.find()
	return bottle.template('viewpatients.tpl', rows = result)
#------------------------------------------------------------------------------

@bottle.route('/organizations')
def organisation_page():
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.organisation_test
	result = collection.find()
	return bottle.template('viewOrganization.tpl',rows = result)
#------------------------------------------------------------------------------

@bottle.route('/patients/edit/<nid>')
def patient_edit_page(nid):
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.patient
	print(nid)
	result = collection.find_one({'nid' : nid})
	return bottle.template('viewEditPatient.tpl',patient = result)
#------------------------------------------------------------------------------

@bottle.route('/patients/view/<nid>')
def patient_view(nid):
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.patient
	print(nid)
	result = collection.find_one({'nid' : nid})
	return bottle.template('viewPatient.tpl',patient=result)
#------------------------------------------------------------------------------

@bottle.route('/addpatient')
def patient_add():
	return bottle.template('viewNewPatient.tpl')
#------------------------------------------------------------------------------
	
@bottle.route('/add_patient')
def patient_add1():
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.patient
	gender = request.GET.get('sex')
	title = request.GET.get('title')
	fname = request.GET.get('firstname')
	mi = request.GET.get('midinitial')
	lname = request.GET.get('lastname')
	address = request.GET.get('address')
	city = request.GET.get('city')
	state = request.GET.get('state')
	zipc = request.GET.get('zip')
	country = request.GET.get('country')
	email = request.GET.get('email')
	tel = request.GET.get('tel')
	dob = request.GET.get('dob')
	nid = request.GET.get('nid')
	bg = request.GET.get('bg')
	weight = request.GET.get('weight')
	height = request.GET.get('height')
	telcc = request.GET.get('telcc')
	occ = request.GET.get('occupation')
	com = request.GET.get('company')
	collection.insert_one({'sex':gender,'title':title,'gname':fname,'mi':mi,
						   'surname':lname,'add':address,'city':city,
						   'state':state,'zip':zipc,'country':country,
						   'email':email,'tel':tel,'dob':dob,'nid':nid,'bg':bg,
						   'weight':weight,'height':height,'telcc':telcc,
						   'occ':occ,'com':com})	
	return bottle.template('viewpatientadd.tpl')
#------------------------------------------------------------------------------

@bottle.route('/edit_patient')
def edit_patient():
	client = pymongo.MongoClient("mongodb://localhost")
	db = client.ClinicalData
	collection = db.patient
	gender = request.GET.get('sex')
	title = request.GET.get('title')
	fname = request.GET.get('firstname')
	mi = request.GET.get('midinitial')
	lname = request.GET.get('lastname')
	address = request.GET.get('address')
	city = request.GET.get('city')
	state = request.GET.get('state')
	zipc = request.GET.get('zip')
	country = request.GET.get('country')
	email = request.GET.get('email')
	tel = request.GET.get('tel')
	dob = request.GET.get('dob')
	nid = request.GET.get('nid')
	bg = request.GET.get('bg')
	weight = request.GET.get('weight')
	height = request.GET.get('height')
	telcc = request.GET.get('telcc')
	occ = request.GET.get('occupation')
	com = request.GET.get('company')
	result = collection.update_one({'nid':nid},{'$set':{
			'sex':gender,'title':title,'gname':fname,'mi':mi,'surname':lname,
			'add':address,'city':city,'state':state,'zip':zipc,'country':country,
			'email':email,'tel':tel,'dob':dob,'nid':nid,'bg':bg,'weight':weight,
			'height':height,'telcc':telcc,'occ':occ,'com':com}})
	print(fname)
	return bottle.template('viewSuccess.tpl',patient=result)

bottle.debug(True)
bottle.run(host='localhost',port=8082)
#------------------------------------------------------------------------------