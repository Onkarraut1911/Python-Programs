from array import *
stu_roll = array('i', [])

n = int(input("Enter number of element : "))

for i in range(n):
    stu_roll.append(int(input("Enter element: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])
