# -----------------------------------------------------------------------------
# Description: Data model for icd10 codes
# Author: Srivatsava
# Date: 26-06-2017
#------------------------------------------------------------------------------

from mongoengine import *

class icd_codes(Document):
	code = StringField(db_field='code', verbose_name='icd code', unique=True)
	disease = StringField(db_field='disease',verbose_name='disease')
	
	def updateUsingDict(self,icdDict):
		word = icdDict[:7].strip()
		self.code = word
		word = icdDict[8:].strip()
		self.disease = word
#------------------------------------------------------------------------------