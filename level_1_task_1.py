#LEVEL 1 TASK 1

def reverse(s):
    str=""
    for i in s:
        str=i +str
    return str
s ="cognifyz"
print("the original string is: ",end="")
print (s)
print ("the reverse string is: ",end="")
print(reverse(s))
