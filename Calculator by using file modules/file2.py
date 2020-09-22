from file1 import *
import file1
#from file1 import add

global indx
print(indx)
print("enter two numbers")
h = int(input("Enter the first number: "))
i = int(input(" Enter the second number : " ))
reslt1 = add(h,i)
reslt2 =sub(h,i)
print(reslt1, "   ",reslt2)