import os
os.system('cls')

#dot notation: first input before the dot, rest in parentheses separated by commas
print("bow".upper())
print("bow".replace("w","y"))

#function composition 
print("bow".replace("w","y").upper())

#Adding a question mark to a string --> by using the escape character \
print("She said \'Hello\' to me")

#function on string
print("string"[2]) #index "string"[x] outputs the x-th letter of a string. Counts from zero.

print(pow.__doc__)  #--> the docstring provides a description of the function power

#Counting from zero
#   Removing zero or more characters from a string (beginning, end, or both) leaves a substring.
#   A prefix is a substring that is formed from "chopping off" zero or more characters from the end.
#   A suffix is a substring that is formed from "chopping off" zero or more characters from the beginning.

#Using a module 
#1. Import a module (only first line of the program)
import math
print(math.fmod(14,12)) #must use math.
print(pow(4,3)) #--> does not produce a floating point number
print(math.pi) 
#   Use functions and constants from the module
print(math.sqrt(25)) #--> produces a floating point number
print(math.pi)
#List everithing in the module 
print(dir(math))
#2. Import a single item
from math import sqrt
print(sqrt(36)) #--> produces a floating point number

#Use the power of from module import * to import everything from the math module 
from math import *

#exponentiation
print(pow(5,3))

#absolute value
print(abs(-3))

#square root 
print(math.sqrt(64))

#Built-in functions for a particular data item e.g. : 97
print(dir(97))

#modulo 
print(math.fmod(14,12))

#All built-in functions 
print(dir(__builtins__))

#User input 
print(input("Enter a string: ")) #-->prints whatever that has been typed by the user

#The computer always interpret the other types as a string
print(2*input("Enter a number: "))
#How to fix this?
print(2*int(input("Enter a number: ")))

#To check type of data
print(type(5))
print(type(5.0))
print(type("halo"))

print(int(5.1))
print(int(5.9))
print(int(-5.9))
print(int("5")) #can't be print(int("4.3")) or print(int("five"))

print(float(5))
print(float(5),float(5.0),float("5.0"),float("5"))
print(str(5),str(5.0),str("5.0"),str("5"))

#Scientific notation
print(2e+10) #--> produces a floating point number
print(2.3e+900)
print(2.3e-900)

#floating point numners are approximate
print(2.00000000000000000000000000000001-2)

#Write a program that prints the total bill, including tax and a 15% tip for a meal that costs $8.00. The tax rate in Ontario is 13%.

#Write a program that prints out the cost of renting a snowboard for 13 days. If you rent a snowboard for five consecutive days, the total cost is $150 for those five days. You can rent it for five-day stretches as you wish, each at this rat. If you rent a snowboard for less than five consecutive , the cost each day is $50. 

#Write a program that ask a user for a number and then print the area of a circle with that number as the radius.
from math import pi
print(pi*pow(int(input("Enter a number: ")),2))

#Displaying strings
print("Double quotes")
print('Single quotes')
print('Hello "py"')
#The escape character \
print("\"Double\" quotes")
#backslash
print("A blackslash \\ is here")

#new line \n
print("Using \'control\' \nfor a new line")

#length of a string len
print(len("Haloo"))
print(len("")) #--> counts from zero
print(len(" "))

#joining substring
print('rain' + 'bow')
#print('rain' + 5) results in error
print('rain' * 5)

#Python uses the slice operation. The slice operation specifies the slicing points for a substring 
##+---+---+---+---+---+---+
#| P | Y | T | H | O | N |
#+---+---+---+---+---+---+
# 0   1   2   3   4   5

#prefix
print("caterpillar"[:5]) #forms cater
#suffix
print("caterpillar"[9:]) #forms ar
#substring
print("caterpillar"[5:9]) #forms pill

#negative indices
print('caterpillar'[5:9])
print('caterpillar'[-6:-2])
print('caterpillar'[-6:9])
print('caterpillar'[5:-2])
print('caterpillar'[5:5])

#upper case
print('BIGsmall'.upper())

#lower case
print('SMALLbig'.lower())

#Only lower case letters can be changed into upper case letters.
#Only upper case letter can be changed into lower case letters.

#Making integers 
import math
print(math.ceil(1.1), math.ceil(1.9))
print(math.floor(1.1), math.floor(1.9))
print(math.trunc(1.1), math.trunc(1.9))
print(math.ceil(-1.1), math.ceil(-1.9))
print(math.floor(-1.1), math.floor(-1.9))
print(math.trunc(-1.1), math.trunc(-1.9))

#truncate --> The int function converts floating point numbers to integers by using truncation

print("string"[2]) #index "string"[x] outputs the x-th letter of a string.

#Finding the middle character of a word with odd numbers of letters.
print(len('mystery')/2) #--> outputs 3.5
import math
print(math.floor(len('mystery')/2)) #outputs 3
print("mystery"[math.floor(len('mystery')/2)])

#Forming a new string from the word "mystery".
#outputting the middle character
from math import floor 
print("mystery"[floor(len('mystery')/2)])
#outputting the first letter of the word
print("mystery"[0])
#changing the middle character with the first letter and vice versa
from math import floor
print("mystery"[math.floor(len("mystery")/2)] + "mystery"[1:math.floor(len('mystery')/2)] + "mystery"[0] + "mystery"[math.floor(len("mystery")/2) + 1:])

#Getting the Current Date and Time

#We can use a function called datetime.now() to retrieve the current date and time.

from datetime import datetime

now = datetime.now()
print(datetime.now())

print(now.year)
print(now.month)
print(now.day)

from datetime import datetime
now = datetime.now()

print('%02d-%02d-%04d' % (now.month, now.day, now.year))
# will print the current date as mm-dd-yyyy
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

print('%02d/%02d/%04d' % (now.month, now.day, now.year) + " " + '%02d:%02d:%02d' % (now.hour, now.minute, now.second))