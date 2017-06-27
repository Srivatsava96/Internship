# -----------------------------------------------------------------------------
# Description: Data model for icd10 codes
# Author: Srivatsava
# Date: 08-05-2017
#------------------------------------------------------------------------------

from mongoengine import *

class icd_codes9(Document):
    code = StringField(db_field='code', verbose_name='icd code', unique=True)
    disease = StringField(db_field='disease',verbose_name='disease')
    
    def updateUsingDict(self,icdDict):
        word = icdDict[:4].strip()
        self.code = word
        word = icdDict[5:].strip()
        self.disease = word