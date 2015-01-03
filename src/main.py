'''
Created on 3 Jan 2015

@author: will
'''
from configLoader import configurationHolder


def runApp():
    config = configurationHolder()
    config.configLoader("/tmp/config")
    value = config.getConfiguration().get("mykey")
    print value
    
if __name__ == '__main__': runApp()
    