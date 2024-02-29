from numpy import*
a = arange(5)
b = arange(5,10)
c = arange(1,10,2)
print(a)
print(b)
print(c)


d= len(c)

for i in range(d):
    print("index",i , ":",c[i])