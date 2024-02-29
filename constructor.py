class Mobile:        #class   #
  def __init__(self ,m,v=80):   #constructor - automaticaly call when make a object of the class
    self.model = m  #asign realme x in model variable   /  This is a instance variable - it write always in the constructor
    self.volume = v  #asign default 80 in the volume variable / This is a instance varible
  
  def  show_model(self , p):    #this is a function  /  instance method
    price = p          #local variable
    print("Model : " ,self.model , "and price ",price)    #access instance variable using self. keyword
    print("Volume : ",self.volume)                   

#passing argument to the constructor
realme = Mobile('Realme x')       #This is object of class Mobile
#actual argument

# accessing method from outside the class
realme.show_model(1000)
realme.model  #accessing instance variable from outside the class
