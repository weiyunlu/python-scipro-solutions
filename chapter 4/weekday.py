"""
Exercise 4.16: Look up calendar functionality
Author: Weiyun Lu
"""

from calendar import weekday
import sys

try:
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
except IndexError:
    print 'You must supply year, month, and day on the command line.'
    sys.exit(1)
except ValueError:
    print 'You have to specify year, month, and day as integers.'

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
wk = days[weekday(year, month, day)]

print 'The day is %s.' %(wk)