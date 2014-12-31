'''
Created on 26 Dec 2014

@author: will
'''

import os

class FileChecker(object):

    _location = "."

    def __init__(self, location):
        self._location = location
        '''
        Constructor
        '''
    
    def haveTheyChanged(self):
        dirlist = os.listdir(self._location)
        for string in dirlist:
            string

class StoreObject(object):

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