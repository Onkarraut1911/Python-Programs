# write a python program to count the occurence of each word in a given string sentence 
string = " This is a sample python program welcome to word of pythone programming "
word = "python"
list = []
wordcount = 0 
list = string.split(" ")
for i in range(0,len(list)) :
    if(word == list[i]) :
        wordcount = wordcount +1
print("Number of occurrences found in the string : ")
print(wordcount)