import os
os.system('cls')

#The changing part in a function is called as parameter

#Avoiding long lines using \
print("Hello,", "How are you", \
"and how is the weather?")

my_string = "Hello,", "How are you", \
"and how is the weather?"

#Phython convention > allow no more than 79 characters on a line

def h(x, y):
    z = (x + y) ** 2
    return z

print(h(1, 2)) 
# Leaving a space between the comma and small is a convention; omitting it does not result in an error.

HEIGHT = 10 #room height
def paint(rooms):
    big = 8 * HEIGHT
    small = 6 * HEIGHT
    one = 2 * (big + small)
    return rooms * one

print(paint(50)) 

WCOST = 100 #cost per week
DCOST = 20  #cost per day
WDAY  = 7   #number of days in a week 
def cost(total_days):
    week = ( total_days // WDAY ) * WCOST
    day = ( total_days % WDAY ) * DCOST
    return week + day

print(cost(32))

import math
LABEL_DIAM = 4  # diameter, in inches
HOLE_DIAM = .25 # diameter, in inches

def area_circle(radius):
    return math.pi * radius ** 2
 
## area of the circle with label radius
outer = area_circle(LABEL_DIAM/2)
## area of the circle with hole diameter
inner = area_circle(HOLE_DIAM/2)
## difference
print(outer - inner)

def f(big, small):
    total = big + small
    return total - big

def g(first, second):
    return f(first + second, first - second)

print(g(2,1))

x = 1
y = x
x = 3
print(x + y)

#avword used in the computer language are not available for use as an identifier. 
# e.g. : for = 4 --> will be error

x = 10
y = 6
y = y + 2
z = x - y
print(z)

#an identifier cannot start with a digit 
# e.g. : 1_number = 1

Total = 10
cost = 3
cost = 5
total = 1
print(Total * cost)

def target(age, rest_heart, intensity):
    max_heart = 220 - age
    reserve = max_heart - rest_heart
    target = rest_heart + intensity * reserve
    return target

print(target(35, 65, .7))

#Write a function volume_cylinder that consumes the diameter in metres and produces the volume of a cylinder of length 2 metres. A function area_circle has been loaded for your convenience.

import math

def areas_circle(rad):
    return math.pi * rad ** 2
    
def volume_cylinder(diameter):
    rad = diameter / 2
    return areas_circle(rad) * 2

#Write a function upper_lower that consumes a string plain and produces a string with the same characters as in plain except that all letters in the first half of the string are in upper case and all the rest of the letters are in lower case. Non-letters should be the same.

import math

def upper_lower(plain):
    first_half = math.ceil(len(plain) / 2)
    return plain[: first_half].upper() + plain[first_half :].lower()
    
print(upper_lower("upper_LOWER"))

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)

def biggest_number(*args):
  print(max(args))
  return max(args)
    
def smallest_number(*args):
  print(min(args))
  return min(args)

def distance_from_zero(arg):
  print(abs(arg))
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if type(city) == type("hi"):
    if city == "Charlotte":
      return 183
    elif city == "Tampa":
      return 220
    elif city == "Pittsburgh":
      return 222
    elif city == "Los Angeles":
      return 475
    else:
      return False
  else:
    return False
  
def rental_car_cost(days):
    cost = 40
    total = days * cost
    if type(days) == int:
      if days >= 7:
        return total- 50
      elif 3 <= days <= 7:
        return total - 20
      else:
        return total
    else:
      return False
      
def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1)\
  + plane_ride_cost(city) + spending_money

print(trip_cost("Los Angeles", 5, 600))