# Write a python program to find the intersection of two list
def intersection(a, b):
    return list(set(a)& set(b))
def main():
    alist =[]
    blist =[]
    n1 = int(input("Enter the number of elements for list1 :  "))
    n2 = int(input("Enter the number of elements for list2 :  "))
    print("For list1 :  ")
    for x in range(0,n1):
        element = int (input("Enter the element" + str(x+1) + ":"))
        alist.append(element)
    print("For list2 :  ")
    for x in range(0,n2):
        element = int (input("Enter the element" + str(x+1) + ":"))
        blist.append(element)
    print("The intersection is :  ")
    print(intersection(alist , blist))
main() 