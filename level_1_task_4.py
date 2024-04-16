#LEVEL 1 TASK 4

#Create a Python program that acts as a basic calculator.

import math
print("Choose the Opeartors:")
print("Your Choose : Addition,Subtraction,Multiplication,Division")
while True:
    choose=input("The operator you want:")
    if choose=="Add":
        a=int(input("Enter a value="))
        b=int(input("Enter b value="))
        c=a+b
        print("Resultant value=",c)
    elif choose=="Sub":
        a=int(input("Enter a value="))
        b=int(input("Enter b value="))
        c=a-b
        print("Resultant value=",c)
    elif choose=="Mul":
        a=int(input("Enter a value="))
        b=int(input("Enter b value="))
        c=a+b
        print("Resultant value=",c)
    elif choose=="Div":
        a=int(input("Enter a value="))
        b=int(input("Enter b value="))
        c=a+b
        print("Resultant value=",c)
    else:
        print("Invalid operator choose!")
