"""
Author: Weiyun Lu
Exercise 7.10: Deduce a class implementation
"""

class Hello:
    def __init__(self):
        pass
    
    def __call__(self,y):
        return 'Hello, ' + y + '!'
        
    def __str__(self):
        return 'Hello, World!'