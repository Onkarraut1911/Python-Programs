from numpy import *
a = array([[10,20,30,40],[50 ,60 ,70 ,80]])
print(a)

n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        [print(a[i][j])]
    print()