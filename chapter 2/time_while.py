"""
Exercise 2.21: Interpret a code
Author: Weiyun Lu
"""

import time
t0 = time.time()
while time.time() - t0 < 10:
    print '...I like while loops!'
    time.sleep(2)
print 'Oh, no - the loop is over.'