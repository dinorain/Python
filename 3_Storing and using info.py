import os
os.system('cls')

#What is a variable or a constant?
#Variable
#   > the name used to refer to some data
#   > the address (location)where the data is stored
#Constant 
#   > the name used to refer to some data
#   > the address (location) where the data  is stored

#For a varible like the cost of living, the address changes
#For a constant like math.pi, the address does not change

#An address is a location in the storage (memory) of a computer

#Using memory

x = 4
y = 2

print(x+y)
print(pow(x,y))
print(pow(x,y)-x)

savings = 100
print(savings)
savings = 200
print(savings)

savings = 100
savings = 300
print(savings)

#Python convention >> use all capitals for names of constants

REVENUE = 100
COST = 30
profit = REVENUE - COST

print(profit)

DAYS_IN_A_WEEK = 7

#variable types are not specified >> easy to change variable's type and using a function on the wrong type is easy

#age is an integer
age = int(input("Enter your age :"))

#Rules and conventions for identifiers
#   1. use letters, numbers, and underscores
#   2. The first character cannot be a number
#   3. No keywords

#It is more understandable and more efficient by using variables

word = "mystery" #string to encode
import math
mid = math.floor(len("mystery")/2)

print(word[mid] + word[1:mid] + word[0] + word[(mid+1):])

#Write a program that prints the area of wrapping paper needed to cover a box with the dimensions specified by the variable assignments in the code box.
width = 45.6
length = 32.1
height = 13.7

print(2 * (width*length + length*height + height*width))

#Write a program that prints the total length of ribbon needed to wrap a box with the dimensions specified by the variable assignments in the code box.

#A box with ribbon tied around its length and width

#The ribbon should cover the top and bottom of the box in both the long and short directions, and should cover each of the four sides once each.

#You should leave another 20 centimetres for tying the bow.

width = 45.6
length = 32.1
height = 13.7
extra = 20

print(2 * (width + length + 2 * height) + extra)

#Write a program that prompts the user for a string of length at least two and then prints a string formed by exchanging the first and last characters in the string provided by the user. 

x = input("Enter a string of two letters at least : ")

print(x[-1] + x[1:len(x) - 1] + x[0])

#Write a program that prompts a user for an input string of length at least two and prints the string with the first half in upper case and the second half in lower case. If the length of the string is odd, the "second half" should be one character longer than the "first half".

word = input("Enter a string : ")
from math import floor
half = floor(len(word) / 2)

print(word[:half].upper() + word[half:].lower())

#The target heart rate can be obtained by adding the resting heart rate to the product of the target intensity (a number between 0 and 1) and the heart rate reserve.

#The heart rate reserve is the difference between the maximum heart rate and the resting heart rate.

#The maximum heart rate is calculated as 220 minus the age.

#For the values given in the code box, print the target heart rate.
age = 35
rest_heart = 65
intensity = .7

max_heart = 220 - age
reserve = max_heart - rest_heart

target_heart = rest_heart + intensity * reserve

print(target_heart)

#Use the += syntax to add a value to an existing variable
#Use the -= syntax to decrease a value to an existing variable
january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

print(annual_rainfall)

#If we want a string to span multiple lines, we can also use triple quotes
haiku = """The old pond,
A frog jumps in:
Plop!"""

print(haiku)

#String Formatting with %

#When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print("Hello %s" % (name))

#The % operator after the string is used to combine a string with variables. The % operator will replace the %s in the string with the string variable that comes after it.

string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

#If you'd like to print a variable that is an integer, you can "pad" it with zeros using %02d. The 0 means "pad with zeros", the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative).
day = 6
print("03 - %s - 2019" %  (day))
# 03 - 6 - 2019
print("03 - %02d - 2019" % (day))
# 03 - 06 - 2019

#Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.

name = "Mike"
print("Hello %s" % (name))

#You need the same number of %s terms in a string as the number of variables in parentheses:

print("The %s who %s %s!" % ("Knights", "say", "Ni"))
# This will print "The Knights who say Ni!"

name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))