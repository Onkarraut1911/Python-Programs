from array import *
stu_roll = array('i', [])
print(" you need to add numbers in array")
print(" if you need to add then type 'yes' another you can type 'no' ")
print(" ")
while (True):
    a = str(
        input(" Again if you need to add then type 'yes' another you can type 'no' : "))
    if (a == "no"):
        break
    if (a == "yes"):
        stu_roll.append(int(input("Enter element for store in the array :")))
        # b= str(input("if you need to add then type 'yes' another you can type 'no' "))
print(" ")
print(" ")

print("This is an array : ")
abc = len(stu_roll)
i = 0
while (i < abc):
    print(stu_roll[i])
    i += 1
