# -----------------------------------------------------------------------------
# Description: Clinical Data Application module with helper functions
# Author: 
# Date: 21-05-2017
#------------------------------------------------------------------------------

import os
import json

class CdApp:
    appName = 'Clinical Data Application'
    appDir = None
    appConf = None
    appDbName = 'ClinicalData'
    
    def __init__(self):
        if not self.appDir:
            self.appDir = os.path.dirname(os.path.dirname(__file__))
    
    @classmethod
    def removeComments(self, file):
        outfile = ''
        lines = file.readlines()
        for line in lines:
            if not line.strip().startswith('//'):
                outfile = outfile + line
        return outfile
    
    @classmethod
    def getAppConfig(self):
        
        if not self.appDir:
            self.appDir = os.path.dirname(os.path.dirname(__file__))

        confPath = os.path.join(self.appDir, 'Data/app.conf')
        with open(confPath, encoding='utf_8') as cf:
            jsonStr = self.removeComments(cf)
            self.appConf = json.loads(jsonStr)
        
        if not self.appConf:
            raise ImportError('Clinical Data Application config is = %s' %self.appConf)
        
        return self.appConf
    
    @classmethod
    def getLogConfig(self):
        if not self.appConf:
            self.getAppConfig()
        
        return self.appConf.get('LogConf')

    @classmethod
    def connectDb(self):
        import mongoengine
        
        if not self.appConf:
            self.getAppConfig()

        mongoengine.connect(self.appConf.get('DbName', 'ClinicalData'), host='localhost', port=27017)
        