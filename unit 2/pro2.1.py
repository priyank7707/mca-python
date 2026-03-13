# 1) Write a program to display basic exception handling in python.

no1=int(input("Enter no1 : "))
no2=int(input("Enter no2 : "))

try:
    ans=no1/no2
    print(ans)
except Exception as e:

    print(e)
