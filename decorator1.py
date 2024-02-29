# def result(marks):
#   for n in marks:
#     if n>=33:
#       pass
#     else:
#       print("Fail")
#       break
#   else:
#     print("Pass")
# result([50,60,40,70,80])

# Decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Function decorated with my_decorator
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
