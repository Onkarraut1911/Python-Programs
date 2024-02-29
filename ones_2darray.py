from numpy import *
a = ones((3,2), dtype=int)
for r in a:
    for c in r: 
        print(c)
    print()