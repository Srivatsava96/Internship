# -----------------------------------------------------------------------------
# Description: Data model for patient
# Author: Srivatsava
# Date: 08-05-2017
#------------------------------------------------------------------------------

from datetime import datetime
from mongoengine import *

class patient(Document):
	
	gender = StringField(db_field='sex', max_length=6, required=True, 
						 verbose_name='gender')
	title = StringField(db_field='title', max_length=15, verbose_name='title')
	givenName = StringField(db_field='gname', max_length=100, required=True, 
						    verbose_name='given name')
	middleInitial = StringField(db_field='mi', max_length=10, 
							    verbose_name='middle name')
	surname = StringField(db_field='surname', required=True, 
						  verbose_name='surname')
	streetAddress = StringField(db_field='add', verbose_name='address')
	city = StringField(db_field='city', verbose_name='city')
	state = StringField(db_field='state', max_length=2, verbose_name='state')
	zipCode = StringField(db_field='zip', max_length=10, 
						  verbose_name='zipCode')
	country = StringField(db_field='country', verbose_name='country')
	email = EmailField(db_field='email', verbose_name='email address')
	telephoneNumber = StringField(db_field='tel', 
								  verbose_name='contact telphone number')
	birthday = DateTimeField(db_field='dob', verbose_name='date of birth')
	nationalID = StringField(db_field='nid', verbose_name='national ID', 
							 unique=True)
	bloodType = StringField(db_field='bg', verbose_name='blood type')
	kilograms = FloatField(db_field='weight', 
						   verbose_name='weight in kilograms')
	centimeters = FloatField(db_field='height', 
							 verbose_name='height in centimeters')
	telephoneCountryCode = StringField(db_field='telcc', 
									   verbose_name='telephone country code')
	occupation = StringField(db_field='occ', verbose_name='occupation')
	company = StringField(db_field='com', verbose_name='company')
	
	def updateUsingDict(self, patDict):
		self.gender = patDict['Gender']
		self.title = patDict['Title']
		self.givenName = patDict['GivenName']
		self.middleInitial = patDict['MiddleInitial']
		self.surname = patDict['Surname']
		self.streetAddress = patDict['StreetAddress']
		self.city = patDict['City']
		self.state = patDict['State']
		self.zipCode = patDict['ZipCode']
		self.country = patDict['Country']
		self.email = patDict['EmailAddress']
		self.telephoneNumber = patDict['TelephoneNumber']
		self.birthday = datetime.strptime(patDict['Birthday'], '%m/%d/%Y')
		self.nationalID = patDict['NationalID']
		self.bloodType = patDict['BloodType']
		self.kilograms = float(patDict['Kilograms'])
		self.centimeters = float(patDict['Centimeters'])
		self.telephoneCountryCode = patDict['TelephoneCountryCode']
		self.occupation = patDict['Occupation']
		self.company = patDict['Company']
#------------------------------------------------------------------------------