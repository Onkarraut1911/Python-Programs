from array import *
stu_id = array('i', [101, 102, 103, 104])
n = len(stu_id)
i = 0
while (i < n):
    print(stu_id[i])
    i += 1

print("which element you need to remove")
a = int(input(" "))
r = stu_id.remove(a)
n = len(stu_id)
i = 0
while (i < n):
    print(stu_id[i])
    i += 1

# print("you removed element : ", r)
