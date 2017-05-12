# -----------------------------------------------------------------------------
# Description: Data model for patient
# Author: Srivatsava
# Date: 08-05-2017
#------------------------------------------------------------------------------

class Patient:
	patCount = 0
	
	def __init__(self,number,gender,title,given_name,midinitial,surname,street_addr,city,state,zip,birthday):
		self.number = number
		self.gender = gender
		self.title = title
		self.given_name = given_name
		self.midinitial = midinitial
		self.surname = surname
		self.street_addr = street_addr
		self.city = city
		self.state = state
		self.zip = zip
		self.birthday = birthday
		Patient.patCount += 1
	def loadOneFile(self):
		return {'number':self.number,'name':{'title':self.title,'given_name':self.given_name,'middle_initial':self.midinitial,'surname':self.surname},'gender':self.gender,'address':{'street_address':self.street_addr,'city':self.city,'state':self.state,'zip':self.zip},'birthday':self.birthday}
