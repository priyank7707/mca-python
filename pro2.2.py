# 2) Write a program to execute user defined exception in python.

class MyError(Exception):
    def __init__(self):
        super().__init__("Invalid age")
        
age=int(input("Enter your age : "))

try:
    if age < 18:
        raise MyError()
    else:
        print("You can vote")
        
except MyError as e:
    print("Error caught",e)