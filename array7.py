from array import *
stu_id = [100, 101, 102, 103]
n = len(stu_id)
i = 0
while (i < n):
    print(stu_id[i])
    i += 1
print("Array after pop")

stu_id.pop()

n = len(stu_id)
i = 0
while (i < n):
    print(stu_id[i])
    i += 1
