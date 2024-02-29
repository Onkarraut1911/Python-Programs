from array import *
stu = array('i', [101, 102, 104, 105, 106])
a = len(stu)
i = 0
while (i < a):
    print(stu[i])
    i += 1

print("Array after reverse : ")
stu.reverse()
a = len(stu)
i = 0
while (i < a):
    print(stu[i])
    i += 1
