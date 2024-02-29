import numpy
array_name = numpy.ones(5)  #numpy.ones(shape , dtype = float , order = 'c')
a = len(array_name)
i = 0
while i < a:
    print('index ', i , '= ',array_name[i])
    i +=1