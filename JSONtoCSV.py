#!/usr/bin/env python
#
# This sctipts reads a json file and output a csv file
# Note:  Does not decompose lower level objects
# Brian McKean
#
import fileinput
import json
import csv
import sys
#
# This part takes a line from the JSON file and
# digs into it to flatten our the nested ojects
# adding labels by concatinating the layered keys with a "."
def flattenDict(d, result=None):
    if result is None:
        result = {}
    
    for key in d:
        value = d[key]
        if isinstance(value, dict):
            value1 = {}
            for keyIn in value:
                value1[".".join([key,keyIn])]=value[keyIn]
            flattenDict(value1, result)
        elif isinstance(value, (list, tuple)):   
            for indexB, element in enumerate(value):
                if isinstance(element, dict):
                    value1 = {}
                    index = 0
                    for keyIn in element:
                        newkey = ".".join([key,keyIn])        
                        value1[".".join([key,keyIn])]=value[indexB][keyIn]
                        index += 1
                    for keyA in value1:
                        flattenDict(value1, result)   
        else:
            result[key]=value
    return result
# 
# Here is the main part
# Reads stdin for a json file
# and sends csv file to stdout
#
lines = [] 
for line in fileinput.input():
    lines.append(line)
myjson = json.loads(''.join(lines))

myDict = []
for x in myjson:
    myDict.append(flattenDict(x))
#
# Create the header for the csv file
#
keys = {}
for i in myDict:
    for k in i.keys():
        keys[k] = 1

mycsv = csv.DictWriter(sys.stdout, fieldnames=keys.keys(),
                       quoting=csv.QUOTE_MINIMAL)
mycsv.writeheader()
for row in myDict:
    mycsv.writerow(row)
   