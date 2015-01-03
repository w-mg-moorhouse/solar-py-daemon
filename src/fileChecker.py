'''
Created on 26 Dec 2014

@author: will
'''

import os

class FileChecker(object):

    _location = "."
    _locationEvaluationList = []

    def __init__(self, location):
        self._location = location
        '''
        Constructor
        '''
    def getFileList(self, location):
        return os.listdir(self._location)
    
    def updateLocationList(self):
        dirlist = self.getFileList(self._location)
        if len(self._locationEvaluationList) == 0:
            for loc in dirlist:
                self._locationEvaluationList.append(StoreLocation(loc))
        else:
            for loc in dirlist:
                addTolist = True 
                for locObj in self._locationEvaluationList:
                    if locObj.getName() == loc:
                        addTolist = False
                        break
                if addTolist == True:    
                    self._locationEvaluationList.append(StoreLocation(loc))

    def evaluateLocationList(self, evaluator):
        pass
                
class StoreLocation(object):

    _evaluated = False
    _listing = None
    
    def __init__(self, fileListing):
        self._listing = fileListing
        
    def getName(self):
        return self._listing
    
    def getEvaluationStatus(self):
        return self._evaluated
    
    def setEvaluationStatus(self, status):
        self._evaluated = status