# -----------------------------------------------------------------------------
# Description: Data model for taxonomy codes
# Author: Srivatsava
# Date: 06-07-2017
#------------------------------------------------------------------------------

from mongoengine import *

class Taxonomy(Document):
    code = StringField(db_field = 'code', unique = True, required = True)
    grouping = StringField(default = None)
    classification = StringField(default = None)
    specialization = StringField(default = None)
    definition = StringField(default = None)
    notes = StringField(default = None)
    
    def updateUsingDict(self,Taxdict):
        self.code = Taxdict['Code']
        self.grouping = Taxdict['Grouping'] or None
        self.classification = Taxdict['Classification'] or None
        self.definition = Taxdict['Definition']or None
        self.notes = Taxdict['Notes'] or None