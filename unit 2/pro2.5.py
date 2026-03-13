# 5) Write a program to read a file and display its contents. At the end it shall
# also display no. of words available in file.

file = open("file.txt","r")
content = file.read()
word = content.split()

print("content of the file : ",content)
print("word of the file : ",word.__len__())

file.close()
