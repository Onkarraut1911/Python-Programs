y = 10    #global variable
def outer():
    z = 15    #Enclosed variable
    def inner():
        x = 4   #Local variable
        nonlocal z   #if you need to modify the enclosed variable then its need to nonlocal keyword
        z = z+1
        print("x :", x)
        print("Inside the function z : ",z)
    inner()
    print("z : ",z)
outer()