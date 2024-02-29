from numpy import *
a = array([100,200,300,400])
b = array([111,200,333,400])
result = a==b
print(any(result)) #anyone is true then 'any' function returns true
print(all(result))  # all is trure then 'all' returns true