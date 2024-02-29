from array import *
abc = array('i', [101, 102, 103, 104, 105])
n = len(abc)
b = 0
while (b < n):
    print(abc[b])
    b += 1

print('array after append')
abc.append(106)


n = len(abc)
b = 0
while (b < n):
    print(abc[b])
    b += 1
