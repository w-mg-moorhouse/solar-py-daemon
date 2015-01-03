'''
Created on 3 Jan 2015

@author: will
'''
from abc import ABCMeta, abstractmethod
from _pyio import __metaclass__

class AbstractEvaluator(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def evaluate(self, fileList):
        pass