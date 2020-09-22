# def fact(z):
#     if z==1:
#         return z
#     else:
#         return z*fact(z-1)
# print(fact(1) )     
#****************************************
# result =z*(z-1)*(z-2)* ...
# # def numb(i):
# #     if(i<=10):
# # #         print(i)
# # #         # i+=1
# # #         numb(i+1)
# # # numb(7)
# # def x():
# #     for i in range(1,7):
# #         for j in range(1,7):
# #             if (i*j==6):
# #                 print(i,"*",j)
# #************************************************
#x= "I bought 15 kg rice and 20kg dal"
def dig(x):
    # a= ("I bounght 15 kg rice and 20kg dal")
    print(x)
    print(len(x))
#dig(x)

def vow(x):
    vowels=0
    for i in range(x):
        if (i=='a'or i=='i'or i=='e'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
            vowels = vowels+i
    print("Number of vowels: ")
    print(vowels)
#

# #st = input("enter the string :")
# vow(x)

#print("enter a string : ")
# st = input("Enter a string ")
# print(st)

# x = " hellow world "
# print("enter the value:" )
# x = input()                

# def add(a,b):
#     c =a + b
#     return c
# def sub(a,b):
#     c =a-b
#     return c 


# h =int(input("enter first no  : ")
# g = int(input(" second Number" ))
# print( " sum = ", add(h,g))
# print (" substract = ",sub(h,g))
# number of words = number of space +1 -number of digit
#               = 4 + 1
# my age
# def spc(x):
#     x = ' '
#     return x
# def dig(d):
#     y = 



# write a program to count the number of given variable in a word
# ct = 0
# wrd = input("Enter the word : ")
# var = input("Enter the variable : ")#a
# for i in wrd:# amazone
#     if(i==var): 
#         ct +=1
        
# print("the number of given character repeated is: " , ct)
def vow(sentence):
    no_of_vowels =0
    for i in sentence:
        if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
            no_of_vowels +=1
    return no_of_vowels
def spc(sentence):
    no_of_spc =0
    for i in sentence:
        if(i==" "):
            no_of_spc +=1
    return no_of_spc
def digt(sentence):
    no_of_digt = 0
    for i in sentence:
        try:
            if (int(i)>=0 and int(i)<=9 ):
                no_of_digt +=1
        except:
            pass
    return no_of_digt
    
def wrds(sentence):
    for i in sentence:
        no_of_wrds = spc(sentence)+1 - digt(sentence)
    return no_of_wrds
    
print(" enter the sentence :")
st = input()
print("number of vowels = ",vow(st))
print("number of space = ",spc(st))
print("number of digits = ",digt(st))
print("number of words = ",wrds(st))
        








