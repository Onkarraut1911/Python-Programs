# Write a python program to check if substring is present or not in given string
def check(str1 , str2) :
    if(str1.find(str2)!=-1):
        print(str2,"Is present in the given string")
    else:
        print(str2,"Is not present in the given string ")
str1 = input("Enter the string ")
str2 = input("Enter the substring ")
check(str1,str2) 