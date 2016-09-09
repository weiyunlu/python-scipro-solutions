"""
Exercise 6.13: Interpret function specifications
Author: Weiyun Lu
"""

from numpy import *
from scitools.StringFunction import StringFunction

def functionify(sentence):
    s = sentence.split(' is a function of ')
    formula = s[0]
    func = "StringFunction('%s'," %formula
    if s[1].find(' with parameter ') != -1:
        sp = s[1].split(' with parameter ')
        variables = [v.strip() for v in sp[0].split(',')]
        parameters = sp[1]
        params = [p.strip() for p in parameters.split(',')]
        func += "independent_variables=['%s'], %s)" %("', '".join(variables),\
                ','.join(params))
    else: #if no parameters, no further splitting of s[1] is necessary
        variables = [v.strip() for v in s[1].split(',')]
        func += "independent_variables=['%s'])" %"', '".join(variables)
    print func
    return eval(func)

with open('text2func.txt', 'r') as infile: #save functions in an array that we can call
    Functions = []
    for line in infile:
        Functions.append(functionify(line))
    
#test run
print Functions #strange unexpected trailing commas, but they don't seem to break anything
print Functions[0](pi/float(2)) #evaluates sin(pi/2)=1.0
print Functions[5](3,4) #does stuff with two variables