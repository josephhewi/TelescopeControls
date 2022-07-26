# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:22:27 2022

@author: josep
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class telescope:
    
    import csv
    #import pandas
    
    def __init__(self):
        self.posn = [0,0,0] # latitude and longitude of physical telescope
        self.aim = [0,0] # location of cosmic body in sky
        self.tgtBase = [0,0] # location of target cosmic body
        self.target = '' # cosmic point of interest
        self.getTargetData() 
    
    def getTargetData(self):
        import csv
        with open('map.csv','r') as csvfile:
            data = csv.reader(csvfile,delimiter=',')
            for row in data:
                if row[0] == self.target.lower():
                    self.tgtDir[0] = row[1]
                    self.tgtDir[1] = row[2]
                    