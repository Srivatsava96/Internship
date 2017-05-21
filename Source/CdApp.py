# -----------------------------------------------------------------------------
# Description: Clinical Data Application module with helper fuctions
# Author: 
# Date: 21-05-2017
#------------------------------------------------------------------------------

import os
import json

class CdApp:
    appName = 'Clinical Data Application'
    appDir = None
    appConf = None
    
    def __init__(self):
        if not self.appDir:
            self.appDir = os.path.dirname(os.path.dirname(__file__))
    
    def removeComments(self, file):
        lines = file.readlines()
        for line in lines:
            line.strip().starts_with(r'//')
            line = ''
        return ''.join(lines)
    
    def getAppConfig(self):
        confPath = os.path.join(self.appDir, 'Data/app.conf')
        with open(confPath, encoding='utf_8') as cf:
            jsonStr = self.removeComments(cf)
            self.appConf = json.loads(jsonStr)
        
        if not self.appConf:
            raise ImportError('Clinical Data Application config is = %s' %self.appConf)
        
        return self.appConf
    
    def getLogConfig(self):
        if not self.appConf:
            self.getAppConfig()
        
        return self.appConf.get('LogConf')
