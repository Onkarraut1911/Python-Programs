def outer():
    x =3
    def inner():
        y = 4
        result = x + y
        return result
    return inner

a = outer()

a()

print(a)
print(a())  #executing this function outside its scope this technique is called as closure
#closure : function object that remembers valued in the enclosing scope even if they are not present in memory