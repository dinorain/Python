import os
os.system('cls')

#Function documentation
# Use ## at line start for greater readibility

#A docstring in Python is put right after the function hrader. 
## multiple lines are fine
## use three double quotes to start and end

#To see docstring :
# print(function_name.__doc__)

#Convention for docstring :
# Summary line starting with triple quote
## states what fuction does
## Relates input and output (if any)
# Blank line
# Details
## Preconditions (data type of input, restrictions)
## Parameters with meaning
## Postconditions (data type of output, side effects)

#Example restrictions on data:
## nonempty strings
## positive integers
## nonzero numbers

#### paper_size

SMALL_2R = 600  # Dimensions in cm of size 2R paper
BIG_2R = 900

SMALL_3R = 1050 # Dimensions in cm of size 3R paper
BIG_3R = 1500

SMALL_4R = 1200 # Dimensions in cm of size 4R paper
BIG_4R = 1800

SMALL_5R = 1500 # Dimensions in cm of size 5R paper
BIG_5R = 2100

def paper_size(small, big):
    """Determines the smallest size of photo paper for a photo of size small x big.

       Preconditions: 
       small: int or float with value > 0
       big: int or float with value > 0

       Parameters:
       small: smaller dimension of photo, in pixels
       big: bigger dimension of photo, in pixels
       The two dimensions can be equal.       

       Returns: string paper size or "Too big"
    """
    if big <= BIG_2R and small <= SMALL_2R:
        return("Use size 2R")      
    elif big <= BIG_3R and small <= SMALL_3R:
        return("Use size 3R")      
    elif big <= BIG_4R and small <= SMALL_4R:
        return("Use size 4R")      
    elif big <= BIG_5R and small <= SMALL_5R:
        return("Use size 5R")      
    else:
        return("Too big")

print(paper_size(900, 1600))
print(paper_size.__doc__)


#making sandwiches

import math

THICKNESS = 1.0 ## in cm, thickness of spread
JAR_VOLUME = 100.0 ## in cubic cm, volume of a jar

def sandwiche(width, length, jars):
    """Determine the number of sandwiches that can be made using bread of size width x length and jars number of jars.

    Preconditions:
    width: int or float with value > 0
    length: int or float with value > 0
    jars: int with value >= 0 

    Parameters:
    width: the width of a piece of bread in cm
    length: the length of a piece of bread in cm
    jars : the number of jars provided

    Returns: int number of sandwiches
    """
    ## compute volume for one sandwiches
    volume_one = width * length * THICKNESS

    ## compute total volume of jar contents
    volume_total = jars * JAR_VOLUME

    ## compute total sandwiches
    return math.floor(volume_total / volume_one)

import math
def sandwiches(width, length, number_jars,
               thickness, jar_volume):
    """Determines the number of sandwiches 
       that can be made

       Preconditions: 
       width: int or float with value > 0
       length: int or float with value > 0
       number_jars: int with value >= 0
       thickness: int or float with value > 0
       jar_volume: int or float with value > 0

       Parameters:
       width: the width of a piece of bread in cm
       length: the length of a piece of bread in cm
       number_jars: the number of jars of spread
       thickness: the thickness of the spread in cm
       jar_volume: volume of each jar in cubic cm

       Returns: int number of sandwiches
    """   
    ## Compute volume for one sandwich
    volume_for_one = width * length * thickness

    ## Compute total volume of jar contents
    volume_available = number_jars * jar_volume 

    ## Compute total sandwiches
    return math.floor(volume_available / volume_for_one)

def pjb(width, length, number_jam_jars, jam_thickness, jam_jar_volume, number_pb_jars, pb_thickness, pb_jar_volume):
    """Determines the number of sandwiches that can be made

       Preconditions: 
       width: int or float with value > 0
       length: int or float with value > 0
       number_jars: int with value >= 0
       thickness: int or float with value > 0
       jar_volume: int or float with value > 0

       Parameters:
       width: the width of a piece of bread in cm
       length: the length of a piece of bread in cm
       number_jars: the number of jars of spread
       thickness: the thickness of the spread in cm
       jar_volume: volume of each jar in cubic cm

       Returns: int number of sandwiches
       """

    ## Compute number of sandwiches worth of jam
    number_jam = sandwiches(width, length,         number_jam_jars,jam_thickness, jam_jar_volume)

    ## Compute number of sandwiches worth of pb
    number_pb = sandwiches(width, length, number_pb_jars, pb_thickness, pb_jar_volume)

    ## Return minimum of values
    return min(number_jam, number_pb)

print(pjb(900, 100, 100, 100, 100, 100, 100, 100))

#### wedding_cake

import math

def area_circle(radius):
    return math.pi * radius ** 2

def volume_cylinder(radius, height):
    return height * area_circle(radius)

def round_cake_spread(radius, height, thickness):
    """Determines volume of frosting of given 
       thickness for a round cake of given 
       radius and height.

       Preconditions: 
       radius: int, float; value > 0
       height: int, float; with value > 0
       thickness: int, float; with value > 0

       Parameters:
       radius: radius of cake, in cm
       height: height of cake, in cm
       thickness: thickness of frosting, in cm

       Returns: float volume of frosting
    """   
    ## Frosting around side
    thick_radius = radius + thickness
    outer = volume_cylinder(thick_radius, height)
    inner = volume_cylinder(radius, height)
    side_frosting = outer - inner

    ## Frosting on top of layer, including side
    top_frosting = area_circle(thick_radius) \
                   * thickness
    
    ## Total frosting
    return top_frosting + side_frosting

def wedding_cake(radius1, radius2, radius3, height1, height2, height3, thickness):
    """Determines volume of frosting of given 
       thickness for a wedding cake of three 
       layers of given radius and height.

       Preconditions: 
       radius1, radius2, radius3: int, float; value > 0
       height1, height3, height3: int, float; value > 0
       thickness: int or float with value > 0

       Parameters:
       radius1, radius2, radius3: radius of cake, in cm
       height1, height2, height3: height of cake, in cm
       thickness: thickness of the frosting, in cm

       Returns: float volume of frosting
    """   
    frosting1 = round_cake_spread(radius1, height1, thickness)

    frosting2 = round_cake_spread(radius2, height2, thickness)

    frosting3 = round_cake_spread
    (radius3, height3, thickness)

    return frosting1 + frosting2 + frosting3

# Debugging is the process of removing errors (bugs)

#### testing in Python
## An assertion contains a Boolean expression.
## An assertion error occurs if the value of the expression is false

def ordinal(num):
    """Docstring here.
    """
    ## Convert integer to a string
    root = str(num)

    ## Determine the ending
    if num % 10 == 1:
        ending = "st"
    elif num % 10 == 2:
        ending = "nd"
    elif num % 10 == 3:
        ending = "rd"
    else:
        ending = "th"

    ## Concatenate the two parts
    return root + ending

def test_ordinal():
    assert ordinal(21) == "21st"
    assert ordinal(642) == "642nd"
    assert ordinal(53) == "53rd"
    assert ordinal(21325) == "21325th"

test_ordinal()

def yarn_size(stitches):
    """Determines yarn size given 4 inches of stitches.

       Preconditions:
       stitches: int > 0; 6 <= value <= 32
     
       Parameter:
       stitches: average number of stitches in 4 inches

       Returns: yarn size
    """
    BULKY_MAX = 15
    if 6 <= stitches <= 11:
        return "Super bulky"
    elif 12 <= stitches <= BULKY_MAX:
        return "Bulky"
    elif 16 <= stitches <= 20:
        return "Medium"
    elif 21 <= stitches <= 22:
        return "Light"
    elif 23 <= stitches <= 24:
        return "Light or Fine"
    elif 25 <= stitches <= 26:
        return "Fine"
    else:
        return "Super fine"

#A baker will offer a "baker's dozen" by giving thirteen items for the cost of twelve. To calculate the total cost, charge for as many "baker's dozens" as possible. The rest of the items will cost either the cost of a dozen, if there are twelve left, or the number of items times the cost of a single item.
DOZEN = 12         # number of items in a dozen
BAKERS_DOZEN = 13  # number of items in a baker's dozen
DOZEN_COST = 10    # cost of a dozen
SINGLE_COST = 1    # cost of a single item
def bakers(items, dozcost, singcost):
    """Determines cost of items with baker's dozen discount.

       Preconditions:
       items: int > 0
       dozcost: int > 0
       singcost: int > 0

       Parameters:
       items: number of items 
       dozcost: cost of a dozen
       singcost: icost of a single item
   
       Returns: total cost with discount of 13 for the cost of a dozen
    """   
    ## Determine numbers of groups of 13 and extras
    total_bd = items // BAKERS_DOZEN
    extras = items % BAKERS_DOZEN
    if items >= 13:
        if total_bd == 1 and extras == 0:
            return total_bd * dozcost
        ## If there are twelve extras, use dozen_cost
        elif total_bd >= 1 and extras == 12:
            return total_bd * dozcost + dozcost
        ## If there are fewer than twelve extras, use single_cost
        elif total_bd >= 1 and extras < 12:
            return total_bd * dozcost + extras * singcost
    elif items == DOZEN:
        return dozcost
    else:
        return items * singcost

def code_ending(entry):
    """determines if the ending
    of the string is ' 9AA'.
    """
    if entry[-4:] == " 9AA":
        return True
    else:
        return False

def code_eight(entry):
    """determines if a string of length 8 is of the right form to be a postal code.
    
       Preconditions:
       entry: string of letters ,digits, spaces only and has length 8
    """
    if len(entry) == 8 and (entry == "AA9A 9AA" or entry == "AA99 9AA"):
        return True
    else:
        return False
    
def uk_code(entry):
    """Determines if a string can be a postal code.

       Preconditions:
       entry: string of letters, digits, spaces only 

       Parameters:
       entry: possible postal code

       Returns "Code" if of one of the following forms:
       "A9 9AA", "A9A 9AA", "A99 9AA", "AA9 9AA",
       "AA9A 9AA", "AA99 9AA" where 9 is any digit and
       A is any letter,
       and "Not code" otherwise
    """

    ## Return "Not code" if the length is not between 6 and 8
    if 6 <= len(entry) <= 8:
        ## Return "Not code" if it does not start with a letter 
        if type(entry[0]) == type("h"):
            ## or end of the form  ' 9AA'
            if code_ending(entry) == True:
                ## Return "Code" for valid codes of length 6
                if len(entry) == 6 and entry == "A9 9AA":
                    return "Code"
                ## Return "Code" for valid codes of length 7
                elif len(entry) == 7 and (entry == "A9A 9AA"\
                or entry == "A99 9AA" or entry == "AA9 9AA"):
                    return "Code"
                ## Return "Code" for valid codes of length 8
                elif code_eight(entry) == True:
                    return "Code"
                ## Return "Not code" for all other inputs
                else:
                    return "Not code"
            else:
                return "Not code"
        else:
            return "Not code"
    else:
        return "Not code"
                    
print(uk_code("A9 9AA"))
print(code_ending("A9 9AA") == True)

import math 

def select_mod(entry, num):
    """Returns the character in entry 
       at position num modulo string length.

       Preconditions:
       entry: string of length > 0
       num: positive integer

       Parameters:
       entry: string containing chosen character
       num: position in the string 

       Return: a single character
    """
    select = int(math.fmod(num, len(entry)))
    return entry[select]

print(select_mod("caterpillar", 13))

def cap_first(entry):
    """Returns string formed from entry 
       with first letter captialized.

       Preconditions:
       entry: string

       Parameter:
       entry: string to be capitalized

       Returns: capitalized string
    """
    if len(entry) == 0:
        return entry.upper()
    else:
        return entry[0].upper() + entry[1:]

print(cap_first("capitalize"))

import math

def exchange(entry):
    """Returns string with middle and last
       character exchanged.

       Preconditions:
       entry: string of odd length > 0

       Parameter:
       entry: string as basis for new string

       Returns: string like entry but with
                middle and last positions exchanged
    """
    if  type(entry) == type("ji") \
    and len(entry) > 0 \
    and len(entry) % 2 == 1:
        mid = int(math.floor(len(entry) // 2))
        last = 2 * mid
        first_part = entry[:mid]
        mid_char = entry[mid]
        second_part = entry[mid+1:last]
        last_char = entry[last]
        return first_part + last_char + second_part + mid_char

print(exchange("caterpillar"))
print(exchange("cat"))

BULLETS = 361
FINE = 321
BRILLIANT = 291
SUPERIOR = 261
LARGE = 231
EXTRA_LARGE = 201
JUMBO = 181
EXTRA_JUMBO = 161
GIANT = 141
COLOSSAL = 121
SUPER_COLOSSAL = 111
MAMMOTH = 101
SUPER_MAMMOTH = 91

def olive_sizes(number):
    """Returns a string for the type of olive
       given the number per kilogram.

       Preconditions:
       number: integer in range from 91 to 351, inclusive

       Parameter:
       number: number of olives in one kilogram

       Return: a string giving type of olive
    """

    if number <= BULLETS:
        return "Bullets"
    elif number >= FINE:
        return "Fine"
    elif number >= BRILLIANT:
        return "Brilliant"
    elif number >= SUPERIOR:
        return "Superior"
    elif number >= LARGE:
        return "Large"
    elif number >= EXTRA_LARGE:
        return "Extra Large"
    elif number >= JUMBO:
        return "Jumbo"
    elif number >= EXTRA_JUMBO:
        return "Extra Jumbo"
    elif number >= GIANT:
        return "Giant"
    elif number >= COLOSSAL:
        return "Colossal"
    elif number >= SUPER_COLOSSAL:
        return "Super Colossal"
    elif number >= MAMMOTH:
        return "Mammoth"
    else:
        return "Super Mammoth"

print(olive_sizes(142))