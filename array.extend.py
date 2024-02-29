from array import *
stu = array('i', [101, 102, 103, 104])
abc = array('i', [105, 106, 107, 108])

a = len(stu)
i = 0
while (i < a):
    print(stu[i])
    i += 1

print("After array extend : ")
stu.extend(abc)
n = len(stu)
i = 0
while (i < n):
    print(stu[i])
    i += 1
