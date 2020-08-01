# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:21:50 2020

@author: susis
"""
## write a function to print the first character of string in the below code * means that we are unsure about the length of string 
## thats why we need to put * otherwise it will just print one word
def String_1(str):
    for x in (str):
        rot= x[0:4]
        return rot

String_1("hello")
# we put star infront 
def first_letter(*abcd):
  for x in abcd:
    ht= x[0]
    return ht
first_letter("hello world")

# Write a function called "divisible_by" that takes two arguments - a number,
#  and a divisor - in that order.  It should return true or false based on whether the number is divisible by the divisor.
a = int(input("Enter any number1: "))
b = int(input("Enter any number2: "))
def divisible_by(a,b):

    divide = a%b
    if divide == 0:
        return True
    else:
       return False
divisible_by(a,b)

# Write a function called "count_e" that takes in one string argument.  It should return the number of "e"s (uppercase or lowercase)
def count_e(teststr):
    
    count = 0
    for i in teststr:
        if  (i=='e' or i== 'E'):
            count += 1
    return count
count_e("GeeksforGeEks")

# Write a function called "double_char" that takes in a string argument.  It should return a string composed of two of each character in the original string.  It might be a little confusing - look at examples below:

# double_char("Hello") returns "HHeelllloo"

# double_char("?33? sw") returns "??3333??  ssww"
def double_char(n, Str):
    word = " "
    for char in Str:
        word += char * n
    return word

print(double_char(2, "Hello"))


import re
def double_char(n, string):
    return re.sub('(.)', r'\1' * n, string)

print(double_char(2, 'Hello'))
