import os
os.system('cls')

#Iteration means repetition; one iteration is one repetition

# While loop recipe
#   Express the task
#   Write a condition
#   Ensure initial values checked in the condition
#   Ensure the condition can change in the loop body

# saying "uncle"
def say_uncle():
    """Docstring here
    """
    response = 'aunt'
    while str(response) != 'uncle':
        response = input("I'll quit if you say 'uncle' :")

say_uncle()

#determininng if a number > 1 is prime

def is_multiple(number, factor):
    return number % factor == 0

def is_prime(num):
    """Determine if num is prime

    Preconditions :
    num: int > 1

    Parameters :
    num: number being checked

    Returns: Boolean (True if num is prime)
    """
    
    factor = 2
    while factor < num :
        if is_multiple(num, factor):
            return False
        factor = factor + 1
    return True

def test_is_prime():
    """Test correctness of is_prime
    """

    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(9) == False
    assert is_prime(50) == False
    assert is_prime(53) == True

test_is_prime()

def is_primee(dig):
    fact = 2
    fails = False
    while fact < dig and not fails:
        fails = is_multiple(dig, fact)
        fact = fact + 1
    return not fails

print(is_primee(50))

def count_chars(entry, char):
    """Determine the number of
       concurrences of char in entry.

       Preconditions:
       entry: a nonempty string
       char: string of length 1

       Parameters:
       entry: the string with character to count
       char: the character to count

       Returns:
       int, nonnegative
    """

    pos = 0
    count = 0
    while pos < len(entry):
        if entry[pos] == char:
            count = count + 1
        pos = pos + 1
    return count

def test_count_chars():
    """Test correctness of count_chars
    """
    assert count_chars("apple", "p") == 2
    assert count_chars("apple", "l") == 1
    assert count_chars("apple", "d") == 0

test_count_chars()
print(count_chars("caterpillar", "l"))

#### pig_latin

def is_vowel(char):
    """Docstring here
    """
    is_a = char == "a" or char == "A"
    is_e = char == "e" or char == "E"
    is_i = char == "i" or char == "I"
    is_o = char == "o" or char == "O"
    is_u = char == "u" or char == "U"
    return is_a or is_e or is_i or is_o or is_u

def is_consonant(char):
    """Docstring here
    """
    return len(char) == 1 and not is_vowel(char)

def first_vowel(word):
    """Determines the first
       vowel in word or 
       length of word if none

       Preconditions:
       word: string of letters only

       Parameter:
       word: a word 

       Returns: int position in word
    """
    ## Start at first position
    pos = 0

    ## Loop over consonants
    while pos < len(word) and is_consonant(word[pos]):
        pos = pos + 1

    ## Return next position
    return pos

def pig_latin(word):
    """Docstring here
    """
    pos = first_vowel(word)
    if pos == 0:
        return(word + "way")
    else:
        return(word[pos:] + word[0:pos] + "ay")

def test_first_vowel():
    """Tests correctness of first_vowel
    """
    assert first_vowel("chrome") == 3  
    assert first_vowel("apple") == 0
    assert first_vowel("sdk") == 3
    assert first_vowel("") == 0

test_first_vowel()

def test_pig_latin():
    """Tests correctness of pig_latin
    """
    assert pig_latin("apple") == "appleway"
    assert pig_latin("chrome") == "omechray"

test_pig_latin()

def repeat_print(num):
    """Prints the input num times.
 
       Preconditions:
       num: positive integer 
    
       Parameter:
       num: the number of times and what is printed

       Side effect: prints num num times.
    """
    count = num
    while count > 0:
        print(num)
        count = count - 1

repeat_print(5)

def increase(num):
    """Determines the sum of num down to 1.

       Preconditions:
       num: int > 0

       Parameter:
       num: the starting number

       Returns: sum of num down to 1
    """
    total = 0
    while num > 0:
        total = total + num
        num = num - 1
    return total

print(increase(5))

def my_power(base, exponent):
    """Determines the product of base to the exponent power.
    
       Preconditions:
       base: int or float, nonnegative
       exponent: int, nonnegative
    
       Returns:
    product of base to the exponent power
    """
    
    mult = base
    while exponent > 1 and type(base) != str and type(exponent) == int:
        mult = mult * base
        exponent = exponent - 1
    return mult
    
print(my_power(5, 5))

## Write a function add_up that adds integers provided by the user, stopping when the user writes "Stop".
def add_up():
    """Adds integers provided by the user, 
       stopping when the user writes "Stop".
       
       Preconditions:
       digit: int 
       
       Returns:
       Added integers
    """
    digit = 0
    add = 0
    while str(digit) != "Stop":
        add = add + int(digit)
        digit = input("Enter an integers: ")
    return add

add_up()

## Write a function no_nums that consumes a string and produces a string which has the same characters as the input but with any digit removed. 
def idnum(wnum, order):
    while len(str(wnum)) -1 >= order and not wnum[order].isdigit():
        order = order + 1
    return order
    
def idstr(wnum, order):
    while len(str(wnum)) -1 >= order and not wnum[order].isalpha():
        order = order + 1
    return order
    
def deldig(wnum):
    pos0 = idnum(wnum, 0)
    posS = idstr(wnum, pos0 + 1)
    posN = idnum(wnum, posS + 1)
    nodig = ""
    while pos0 <= len(str(wnum)) - 1 and posS <= len(str(wnum)) - 1:
        nodig = nodig + wnum[:pos0] + wnum[posS:posN]
        
        posS = idstr(wnum,posN + 1)
        pos0 = idnum(wnum, posS + 1)
    return nodig
    
def deldigS(wnum):
    pos0 = idnum(wnum, 0)
    posS = idstr(wnum, pos0 + 1)
    posN = idnum(wnum, posS + 1)
    nodig = ""
    while pos0 <= len(str(wnum)) - 1 and posS <= len(str(wnum)) - 1:
        nodig = nodig + wnum[:pos0] + wnum[posS:posN]

        posS = idstr(wnum,posN + 1)
        pos0 = idnum(wnum, posS + 1)
    return posS
    
def deldig0(wnum):
    pos0 = idnum(wnum, 0)
    posS = idstr(wnum, pos0 + 1)
    posN = idnum(wnum, posS + 1)
    nodig = ""
    while pos0 <= len(str(wnum)) - 1 and posS <= len(str(wnum)) - 1:
        nodig = nodig + wnum[:pos0] + wnum[posS:posN]

        posS = idstr(wnum, posN + 1)
        pos0 = idnum(wnum, posS + 1)
    return pos0
    
def no_nums(wnum):
    """Produces a string which
       has the same 
       characters as the input but with 
       any digit removed. 
       
       Preconditions:
       wnum: str
       
       Parameters:
       wnum: the inputed string, str with digit(s)
       
       Returns:
       a string which has the same characters as 
       the input but with any digit removed.
    """

    pos0 = idnum(wnum, 0)
    if type(wnum) == type(1) or pos0 == 0:
        return ""
    elif pos0 != 0:
        posS = deldigS(wnum)
        posN = deldig0(wnum)
        if posN >= posS \
        and type(wnum[posS:]) == type("H") :
            return deldig(wnum) + wnum[posS:]
        elif type(wnum) == type("H"):
            return wnum
    else:
        return wnum
    
print(idnum("hol5555555aa55a", 0))
print(idstr("hol5555555aa55a", 4))
print(idnum("hol5555555aa55a", 11))
print(idstr("hol5555555aa55a", 13))
print(deldig0("hol5555555aa55a"))
print(deldigS("hol5555555aa55a"))
print(len("hol5555555aa55a"))
print(no_nums("hol5555555aa55a"))
print(no_nums("hol5555555aa55a"))
print(no_nums("hhhhhhhh"))

