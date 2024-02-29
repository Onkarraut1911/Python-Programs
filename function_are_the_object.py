def f():
    print("hi")

f()
f     #function object reference(this is a function adress)
g = f  #asign function adress in g
g()   #this is same function f() = g()
      
# if you call function without parantheses it will give that function reference 