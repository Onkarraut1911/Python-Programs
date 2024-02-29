from numpy import *
ab = int(input("Enter rows of the array : "))
ac = int(input("Enter column of the array : "))
a = zeros((ab, ac), dtype=int)

i = 0
while i < ab:
    j = 0
    while j < ac:
        # print("Enter elements : ")
        # el = int(input("Enter elements in the index [",i,"][",j,"]"" : "))
        el = int(input("Enter elements : "))
        a[i][j] = el
        j += 1
    i += 1


print(" ")

i = 0
while i < ab:
    j = 0
    while j < ac:
        # print(a[i][j])
        print(" index [",i,"][",j,"]"" : ",a[i][j])
        j += 1
    i += 1

print(a)
