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
