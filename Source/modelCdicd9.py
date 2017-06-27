# -----------------------------------------------------------------------------
# Description: Data model for icd9 codes
# Author: Srivatsava
# Date: 27-06-2017
#------------------------------------------------------------------------------

from mongoengine import *

class icd_codes9(Document):
    code = StringField(db_field='code', verbose_name='icd code', unique=True)
    disease = StringField(db_field='disease', verbose_name='disease')
    
    def updateUsingDict(self,icdDict):
        word = icdDict[:5].strip()
        self.code = word
        word = icdDict[6:].strip()
        self.disease = word
#------------------------------------------------------------------------------