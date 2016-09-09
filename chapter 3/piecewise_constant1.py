"""
Exercise 3.26: Implement a piecewise constant function
Author: Weiyun Lu
"""

def piecewise(x, data, endpoint):
    testint = 1 #we must test the interval points are increasing and the endpoint is above them all!
    value = 0 #the output of the function
    for i in range(1,len(data)):
        if data[i][1] <= data[i-1][1]:
            testint = 0
    if endpoint <= data[-1][1]:
        testint = 0
    success = (data[0][1] <= x and x <= endpoint and testint == 1)
    msg = "Type error!  The interval points must be increasing, and x must be in the specified range!"
    assert success, msg
    for i in range(len(data)-1):
        if data[i][1] <= x <= data[i+1][1]: #if x in [x_i, x_{i+1}], return v_i
            value = data[i][0]
    if data[-1][1] <= x <= endpoint: #if x in [x_n, {x_n+1}], return v_n
        value = data[-1][0]
    return value
    
A = [[-1,0],[0,1],[4,1.5]]
end = 2

print 'Let us test the function f: [0,1] -> -1, [1,1.5] -> 0, [1.5,2] -> 4.'
print 'The value at 0.5 is %f.' %(piecewise(0.5,A,end))
print 'The value at 1.2 is %f.' %(piecewise(1.2,A,end))
print 'The value at 2 is %f.' %(piecewise (2,A,end))