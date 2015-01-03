
class configurationHolder(object):
    configuration = {}
    
    def __init__(self):
        self
    
    def addToConfiguration(self, key, value):
        self.configuration[key] = value
        
    def getConfiguration(self):
        return self.configuration

    def configLoader(self, configLocation):
        config = open(configLocation, 'r')
        for line in config:
            values = line.split("=")
            if len(values) == 2:
                self.addToConfiguration(values[0], values[1])
