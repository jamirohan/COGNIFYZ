#LEVEL 1 TASK 5

#Write a Python function that checks whether a
#given string is a palindrome

x=input("Enter a String value=")
palindrome=x[ : :-1]
if palindrome==x:
    print(x,"is Palindrome")
else:
    print(x,"is not a palindrome")
