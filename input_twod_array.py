from numpy import *
a = int(input("Enter Number of Row: "))
b = int( input("Enter Number of columns: "))
a = zeros((a,b), dtype=int)
u = len(a)
print(a)
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter Elements"))
        a[i][j]=x

for i in range(u):
    for j in range(len(a[i])):
        print(a[i][j])
print(a)



for r in a :
    for c in r:
        print(c)
print(a)