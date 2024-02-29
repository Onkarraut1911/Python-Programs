import numpy
stu_roll = numpy.array([10,20,30,40,50],dtype=float)
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])

stu_char = numpy.array(['a','b','c','d'])
print(stu_char)
print(stu_char.dtype)

stu_name = numpy.array(["sonam","sonali","shamal"])
print(stu_name)

stu_name[1]="mohan"
print(stu_name)
