from numpy import *
a = array([1,2,3,4,5])
b = ones(5,dtype = int)
c = a + b

d = len(c)
for i in range(d):
    print('index ',i,'=',c[i])