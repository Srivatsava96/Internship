# -----------------------------------------------------------------------------
# Description: Data model for taxonomy codes
# Author: Srivatsava
# Date: 06-07-2017
#------------------------------------------------------------------------------

from mongoengine import *

class Taxonomy(Document):
    code = StringField(db_field = 'code', unique = True, required = True)
    grouping = StringField()
    classification = StringField()
    specialization = StringField()
    definition = StringField()
    notes = StringField()
    
    def updateUsingDict(self,Taxdict):
        self.code = Taxdict['Code']
        self.grouping = Taxdict['Grouping']
        self.classification = Taxdict['Classification']
        self.definition = Taxdict['Definition']
        self.notes = Taxdict['Notes']