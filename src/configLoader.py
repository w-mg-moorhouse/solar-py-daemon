
def configLoader(configLocation):
    config = open(configLocation, 'r')
    for line in config:
        values = line.split("=")