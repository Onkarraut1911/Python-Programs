class Mobile:
    fp = 'Yes'

    @classmethod
    def is_fp(cls):
        print("Finger Print:", cls.fp)

#This is objects of class Mobile
realme = Mobile()     
redmi = Mobile()
geek = Mobile()

print("Class FP : ", Mobile.fp)       
print("RealMe:", realme.fp)             #if we change vlaue of class variable using object then it change for this object not other object

print("Redmi:", redmi.fp)
print("Geeky:", geek.fp)
print()

Mobile.fp = 'No'     #if we change value of class variable using classname as a object then it is changed for all the object

print("Clas FP : ", Mobile.fp)
print("RealMe:", realme.fp)

print("Redmi:", redmi.fp)
print("Geeky:", geek.fp)
