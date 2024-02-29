# write a python python program to map to lists into a dictionary
keys = []
values = []
n = int(input("Enter number of elements for dictionary : " ))
print("For keys : ")
for x in range(0,n):
    element = int (input("Enter element " + str(x+1) + ": "))
    keys.append(element)
print("for values :  ")
for x in range (0 , n):
    element = int (input("Enter element " + str(x+1) + ": "))
    values.append(element)
d = dict(zip(keys,values))
print("Enter dictionary is : ")
print(d)