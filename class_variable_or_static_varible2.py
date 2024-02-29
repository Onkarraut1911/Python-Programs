class Mobile:
  fp ='Yes' #class variable
  def __init__(self):
    self.model = 'Realme X'  #instance variable
  def show_model(self):
    print(self.model)

  @classmethod   #classmethod
  def is_fp(cls): #class method with cls as first parameter
    cls.fp      #access class variable using cls.variable_name

realme = Mobile()

Mobile.fp  #accessing class variable outside the class 
print(Mobile.fp)
Mobile.is_fp()        #call class method  
