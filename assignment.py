#write a python program to sum all the items in a list
#ans using a for loop
#num=[8,2,3,0,7]
#total=0
#for x in num:
#    total +=x
#    print(total)

# ans using sum method
#a=[8,2,3,0,7]
#num=sum(a)
#print(num)

# 2 write a python program to reverse a string.
#reverse "1234abcd"
#word= "1234abcd"[::-1]
#print(word)
#
#example2
#name="agwu david okorie"[::-1]
#print(name)


#example 3
#reverse "hello world"
#txt="hello world"[::-1]
#print(txt)

#create a function that takes a string as an argument
#def my_function (x):
#    return x [::-1]
#text=my_function("where are you from :")
#print(text)

#example 1
#def my_function(x):
#    return x[::-1]
#txt=my_function("how old are you")
#print(txt)

# 3 write a python function that takes a number as a parameter and check if the number is prime or not
#number= int(input("enter any number :"))
#if number > 1:
#    for i in range(2, number):
#        if(number % i) == 0:
#            print(number, "is not a prime number")
#            break
#        else:
#            print(number,"is a prime number")

#write a python program to check if a string is a pangram or not
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("the quick brown fox jumps over the lazy dog"))
