# Wright a python program to find the union of two lists 
first_list = []
second_list = []
count_first_list = int(input("Enter a total number of first list "))
for i in range(1,count_first_list +1) :
    no = int(input("Enter a number"))
    first_list.append(no)
count_second_list = int(input("Enter a total number of second list "))
for i in range(1,count_second_list + 1) :
    no = int(input("Enter a number "))
    second_list.append(no)
print("First list ",first_list)
print("second list ",second_list)
final_list = list (set(first_list + second_list))
print("Final list",final_list)