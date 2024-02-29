def add():
    a= int(input("Enter a first number : "))
    b= int(input("Enter a second number : "))
    result = a + b
    return result





def outer(add):
     def inner():
         result = add()
         c = int(input("Enter third number : "))
         result += c
         return result
     return inner


#@outer  #add = outer(add)

print("Addition is : ",add())