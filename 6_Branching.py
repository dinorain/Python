import os
os.system('cls')

#Technique for different cases : branching

#In CS, branches can rejoin later

#chocolate sales
BAR_COST = 2  #cost of a bar of chocolate

def is_yes(word):
    return word[0] == "Y" or word[0] == "y"

##ask user for number of bars 
bars = int(input("Enter number of bars : "))

##compute the cost of chocolate
cost = bars * BAR_COST

##ask user if donation is desired
donate = input("Donate $10 ? ")

if is_yes(donate):
    cost = cost + 10
print("$" + str(cost))

#odd-length string
def is_odd_string(word):
    if len(word) % 2 == 1:
        return True
    else:
        return False

print(is_odd_string("a"))
print(is_odd_string("ab"))

#simplified Pig Latin
##word nonempty, consists of letters only
def is_vowel(word):
    return word[0] == "a" or word[0] == "A" or word[0] == "e" or word[0] == "E" or word[0] == "i" or word[0] == "I" or word[0] == "o" or word[0] == "O" or word[0] == "u" or word[0] == "U"


def easy_pig(word):
    if is_vowel(word):
        part = word + "w"
    else:
        part = word[1:] + word[0]
        
    return part + "ay" 

#Shorter code can be
def shorter_pig(word):
    if is_vowel(word):
        return word + "w" + "ay"

    return word[1:] + word[0] + "ay"

print(easy_pig("hello"))
print(shorter_pig("ello"))

def offpeak(hour):
    if hour < 9 or hour > 17:
        return("Off peak")
    else:
        return("Peak")

print(offpeak(7))
print(offpeak(9))
print(offpeak(20))

#More than two sets of instructions

def size(mass):
    if mass >= 70:
        return("Jumbo")
    elif mass >= 63:
        return("Extra Large")
    elif mass >= 56:
        return("Large")
    elif mass >= 49:
        return("Medium")
    elif mass >= 42:
        return("Small")
    else:
        return("Peewee")

print(size(45))
print(size(90))

#Three questions with nested branching

def guess(digit):
    if digit < 5:
        if digit < 3:
            if digit < 2:
                return 1
            else:
                return 2
        else:
            if digit < 4:
                return 4
            else:
                return 3
    else:
        if digit < 7:
            if digit < 6:
                return 5
            else:
                return 6
        else:
            if digit < 8:
                return 7
            else:
                return 8

print(guess(6))

x = 3
y = 10
if x > 0:
   y = 12
y = y + 5
print(y)

x = -3
y = 10
if x > 0:
   y = 12
y = y + 5
print(y)

x = -3
y = 10
if x > 0:
   y = 12
   y = y + 5
print(y)

def choose(x):
    if not x < 5:
        return "Yes"
    else:
        return "No"

print(choose(y))

def choose1(x):
    if x < 5 or x > 90:
        return "Yes"
    else:
        return "No"

print(choose(y))

def bigger(x, y):
    if x > y:
        return x
    else:
        return y

#Write a function total_bill that consumes the cost of merchandise, age in years, and tax rate and produces the total bill, where there is a discount of 10% for ages of at least 65. The discount is applied before the tax is computed. The tax is given as a number between 0 and 1.

def total_bill(cost, age, tax):
    if age >= 65:
        return (1 + tax) * (0.9 * cost)
    else:
        return (1 + tax) * cost
    
#Write a function greeting that consumes a string of length at least three and produces "Hello" if the first three characters are "Hi!" and produces "Bye" otherwise.
def greeting(string):
    if len(string) >= 3:
        three = string[:3]
        if three == "Hi!":
            return "Hello"
        return "Bye"
    return "Bye"

#Write a function is_time that consumes two integers, one representing hours in 24-hour time and the other minutes in 24-hour time.

#The function should produce "Passes" if the values are legal values for a time (that is, from 0 to 23 for hours and from 0 to 59 for minutes), and "Fails" otherwise. 

def is_time(hour, minute):
    if 0 <= hour <= 23 \
        and 0 <= minute <= 59:
        return "Passes"
    return "Fails"

x = 8
if x < 6:
    if x > 3:
        x = x + 1
    else:
        x = x - 1
else:
    if x > 9:
        x = x + 2
    else:
        x = x - 2

print(x)

x = 120
if x > 0:
   print("pos")
elif x < 0:
   print("neg")
else:
   print("zero")

#Write a function max_of_three that consumes three numbers and produces the maximum of the three numbers. The numbers do not need to be distinct.
def max_of_three(x, y, z):
    if x >= y >= z or x >= z >= y:
        return x
    elif y >= x >= z or y >= z >= x:
        return y
    elif z >= x >= y or z >= y:
        return z
#Write a function total_bill that consumes the cost of merchandise, age in years, and tax rate and produces the total bill, such that:

## there is a discount of 10% for ages of at least 65, applied before the tax is computed or the shipping charge added
## there is a shipping charge of $5 for all purchases of less than $100 (where the value is the purchase is considered before the discount is applied, if any, and does not include tax)

#The percentage tax rate is given as a number between 0 and 1. 
def total_bill1(cost, age, tax):
    if age >= 65:
        before65 = (1 + tax) * (0.9 * cost)
        if before65 <= 100:
            return before65 + 5
        return before65
    else:
        before = (1 + tax) * cost
        if before <= 100:
            return before + 5
        return before

#Write a function integer_type that consumes a value of any type and produces "Even integer" if it is an even integer, "Odd integer" if it is an odd integer, and "Not an integer" otherwise.
def integer_type(anything):
    if type(anything) == type(1) and anything % 2 == 0:
        return "Even integer"
    elif type(anything) == type(1) and anything % 2 == 1:
        return "Odd integer"
    else:
        return "Not an integer"

#Write a function off_peak that consumes any type of data and determines if the time is eligible for off peak rates. Your function should produce one of the following outputs: "Off peak", "Peak", and "Not a time". Off-peak rates are based on 24-hour time, for values less than 9 or greater than 17.
def off_peak(time):
    if type(time) == type(1) and \
    (0 <= time < 9 or 17 < time <= 23):
        return "Off peak"
    elif type(time) == type(1) and \
    9 <= time <= 17:
        return "Peak"
    else:
        return "Not a time"

#Write a function leap_year that consumes a positive integer and produces "Leap year" if it is a leap year and "Common year" otherwise. A year is a leap year if it is a multiple of 4, 100, and 400, or if it is multiple of 4 but not a multiple of 100.

def is_multiple(number, factor):
    return number % factor == 0
    
def leap_year(year):
    of_4 = is_multiple(year, 4)
    of_100 = is_multiple(year, 100)
    of_400 = is_multiple(year, 400)
    if type(year) == type(1) and of_400:
        return "Leap year"
    elif type(year) == type(1) and of_4 and not of_100:
        return "Leap year"
    else:
        return "Common year"
    
print(leap_year(4))
print(leap_year(100))
print(leap_year(400))

def romanize(digit):
    tipe = type(digit) == type(1)
    if tipe and digit <= 3:
        if digit == 3:
            return "III"
        elif digit == 2:
            return "II"
        else:
            return "I"
    elif tipe and digit <= 6:
        if digit == 6:
            return "VI"
        elif digit == 5:
            return "V"
        else:
            return "IV"
    elif tipe and digit <= 10:
        if digit == 10:
            return "X"
        elif digit == 9:
            return "IX"
        elif digit == 8:
            return "VIII"
        else:
            return "VII"
    