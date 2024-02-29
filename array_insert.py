from array import *
stu_roll = array('i', [100, 101, 102, 103])
n = len(stu_roll)
i = 0
while (i < n):
    print(stu_roll[i])
    i += 1

print("Array after Insert")
stu_roll.insert(1, 106)
stu_roll.insert(3, 150)

n = len(stu_roll)
i = 0
while (i < n):
    print(stu_roll[i])
    i += 1
