from array import *
stu_roll = array('i', [101, 102])
n = len(stu_roll)
i = 0
while (i < n):
    print(stu_roll[i])
    i += 1

a = int(input("Which poition of element you need to remove under the :"))
print("you removed ", a + 1)
r = stu_roll.pop(a)

n = len(stu_roll)
i = 0
while (i < n):
    print(stu_roll[i])
    i += 1

print("you removed element : ", r)
