from numpy import *
a = array = ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0,]])
n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j += 1
    i += 1
    print()
    