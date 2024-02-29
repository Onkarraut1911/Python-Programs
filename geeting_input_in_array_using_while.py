from numpy import *
b = int(input("Enter a number of elements : "))
n = zeros(b, dtype=int)
d = len(n)
i = 0

while (i < d):
    x = int(input("Enter elements : "))
    n[i] = x
    i += 1

i = 0

while (i < d):
    print(n[i])
    i += 1
