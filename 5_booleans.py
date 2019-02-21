import os
os.system('cls')

print("\n") #outputs blank lines

#A boolean has two possible values : True or False
#In Python, "or" is used to mean "one or the other or both"

#A condition using "and" is True when ALL smaller expressions are True

#A condition using "or" is True when AT LEAST ONE smaller expression is True

print(True or False)
print(True and False)
print(not False)

print("True")
print(True)
print(type("True"))
print(type(True))

#Do not use quotation marks on Booleans True and False

#equality ==
#inequality !=

print("True" == True)
print("True" != True)

# multiple comparisons can be  made on one line 
print(3 < 4 < 5)
print(3 <= 4 < 2) # False
print(3 == 3 >= 3)

#can be used to compare strings
print("A" != "a")
print("ape" <= "cat")
print("cat" == "cat")

print("cat" < "cat")

#using and
num = 10
print((10 <= num) and (num <= 20))
print(10 <= num <= 20)

#using or
age = 35
print((age < 21) or (65 < age))

#Python's approach to Booleans
print("False" and "True")
print("cat" or "dog")
print(True + 4)

#Non-Booleans masquerading as Booleans
# False : None, False, 0, 0.0, ""
# True : Almost everything else

#avoid using Boolean functions on non-Boolean values
#avoid using mathematical functions on Boolean values

#Unicode is an international standard for encoding. It maps each character to a number (code point)
#the order of the maps : blank.. punctuation..digits(in order).. upper case letters (in order).. lower case letters (in order)


#code point from character 
print(ord("A"))
#character from code point
print(chr(65))

#more string functions
#   Letter
print("My string".isalpha())
print("m".isalpha())

#   lower case
print("MY".islower())
print("my".islower())

#   upper case
print("my".isupper())
print("MY".isupper())

#   number
print("7".isdigit())
print("seven".isdigit())

#   blank
print("".isspace())
print(" ".isspace())
print(".".isspace())

#determining if a number is even
from math import floor
def even(num):
    return floor(num / 2) == num / 2

from math import ceil
def odd(num):
    return ceil(num / 2) != num / 2

#from math import fmod
#def even(num):
#    return fmod(num,2) == 0

print(even(5))
print(even(66))
print(odd(5))
print(odd(66))

#using "and" in a function
#def is_multiple(num,fac):
#    return num % fac == 0

#what if the fac inputted is 0?
def is_multiple(num,fac):
    return fac != 0 and num % fac == 0

print(is_multiple(10,5))
print(is_multiple(10,0))
print(is_multiple(10,7))

#def starts_with_a(word):
#    return word[0] == "a"

#what if the string is empty?
def starts_with_a(word):
    return len(word) > 0 and word[0] == "a"

print(starts_with_a("hello"))
print(starts_with_a("apple"))
print(starts_with_a(""))


print(not 5 < 3) ## Since 5 is not less than 3, the value of the expression is not False, which has the value True.

print(not ((1 < 2) and (2 < 4))) ## The condition using and has value True since both smaller expressions have value True. This makes the value of the condition be not True, which is False.

print((3 < 4) or (not (2 < 5))) ## Correct: The first smaller expression has the value True. Since a condition using or has value True if any smaller expression has the value True, here the condition has the value True.

print((not (3 < 4)) or (not (2 < 5))) ## Both smaller expressions have the value not True, hence False. Since a condition using or has value False if all smaller expressions have the value False, here the condition has the value False.

print(not ((3 < 4) or (2 < 5)))

## x <= y has the same value as:
### not (x > y)
### (x < y) or (x == y)
### (x <= y) and (3 < 4)
### (1 < 0) or (x <= y)

#For which of the possible values of the variable my_string does the comparison my_string < "apple" have the value True? There may be more than one correct choice.

print("ape" < "apple")
#Correct: The third character of "ape" comes before the third character of "apple".

print("A" < "apple")
#Correct: The upper-case letter "A" comes before the lower-case letter "a".

print("5 apples" < "apple")
#Correct: The number 5 comes before the lower-case letter "a".

#This and That (or This, But Not That!)

#Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

#    not is evaluated first;
#    and is evaluated next;
#    or is evaluated last.


print(chr(5))
# outputs the character at the order 5  

print(ord(chr(5)))
# outputs the order of the character

print(ord("6"))

#Write a function is_big that consumes a number, produces True if the number is at least 100, and produces False otherwise.
def is_big(number):
    return number >= 100 

print(is_big(150))

# Write a function is_odd_string that consumes a string, produces True if it has an odd number of characters, and produces False otherwise.
def is_odd_string(string):
    odd = len(string) % 2 != 0 
    return odd

print(is_odd_string("halo"))

# Write a function is_adult that consumes an integer age, produces True if it is at least 21 and at most 65, and produces False otherwise.
def is_adult(age):
    return 21 <= age <= 65

print(is_adult(18))

# Write a function is_yes that consumes a nonempty string, produces True if it starts with a y (either lower-case or upper-case), and produces False otherwise.
def is_yes(string):
    first = string[0]
    return first == "y" or first == "Y"
    
print(is_yes("yes"))

def tester(num1, num2):
    return num1 > num2 and \
    num1 < 100 and \
    num2 % 10 == 0 

print(tester(121, 120))

def seatbelt(age, weight, height):
    return age >= 8 or weight >= 36 or height >= 145

print(type("haloo"))

#Write a function good_string that consumes a string, produces True if the first character is a letter and the second character is either a digit or a blank space, and produces False otherwise.

def good_string(string):
    first = string[0]
    second = string[1]
    return first.isalpha() \
    and (second.isdigit() or second.isspace())

print(good_string("a halo"))

x = 50
print((60 % x == 3) and (x != 0))
# if x = 0 --> There will be an error message. The first smaller expression will be evaluated before the second smaller expression. Using zero as the second value in a remainder calculation results in an error, since it requires division by zero.

x = 0
print((x != 0) and (60 % x == 3))

x = "super"
print(x[0] == "s" and len(x) > 3)
#if x = "", there will be an error message. Trying to find the first character in an empty string results in an error message.

x = ""
print(len(x) > 3 and x[0] == "s")

#Select the ordering of the three conditions to be joined by and so that there will be no error messages, no matter what the input x is, or indicate that no ordering is possible.
#3,2,1
#(1) x[0] == "a"
#(2) len(x) > 0 
#(3) type(x) == type("")

#Select the ordering of the three conditions to be joined by or so that there will be no error messages, no matter what the input x is, or indicate that no ordering is possible.
#No ordering is possible.
#(1) x[0] == "a"
#(2) len(x) > 0 
#(3) type(x) == type("")

#Select the ordering of the three conditions to be joined by or so that there will be no error messages, no matter what the input x is, or indicate that no ordering is possible.
# 1,3,2
#(1) type(x) != type("")
#(2) x[0] == "a"
#(3) len(x) == 0

#Order the smaller expressions joined by and's in such a way that there is no error message for any type of input.
def order_ands(any):
    return type(any) == type(1)\
    and any + 1 > 5 \
    and any % 2 == 0 \

#Order the smaller expressions joined by or's in such a way that there is no error message for any type of input.
def order_ors(any):
    return type(any) != type("") \
    or len(any) < 2 \
    or any[1] == "a"

#We can check the type of a variable by seeing if its type is the same as the type of a constant. For example, to check if a variable x is an integer, you can use the expression type(x) == type(1).

#Write a function even_int that consumes any type of data, produces True if it is an even integer, and produces False otherwise.
def even_int(any):
    return type(any) == type(1) and any % 2 == 0

#Write a function four_i that consumes any type of data, produces True if it is a string with the letter i (lower-case) in position 4 (index 3), and produces False otherwise.
def four_i(anyk):
    return type(anyk) == type("hi") \
    and len(anyk) >= 4 \
    and anyk[3] == "i" \
    
print(four_i("woww"))