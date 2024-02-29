y = 10
def inner():
    x = 4
    global y
    y = y+1 #global function not modified in the function if it is need  then use a keyword global then moeified a varible
    
    print("x: ",x)
    print("inside the function y : ",y)

print("y :",y)
inner()

print("y :",y)