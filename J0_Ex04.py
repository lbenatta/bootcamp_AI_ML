import re
import string

txt = str (input ("Enter your text here:"))

# ---- Part 1. text_analyzer

def text_analyser(my_txt):
    if txt != str:
        print("Error message: this txt is no a string")

def py_isupper(text): 
    S1 = sum(1 for c in text if c.isupper())
    #return sum(1 for c in text if c.isupper())
    print("Sum_upper :", S1)
py_isupper(txt)

def py_islower(text): 
    S2 = sum(1 for c in text if c.islower())
    print("Sum_lower :", S2)
py_islower(txt)

def py_ispunct(text): 
    punc = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    S3 = sum(1 for c in text if c in punc)
    print("Sum_punct :", S3)
py_ispunct(txt)

def py_isspace(text): 
    space = " " 
    S4 = sum(1 for c in space)
    print("Sum_space :", S4)
py_isspace(txt)

# ---- Part 2.  __name__==__main__

if __name__ == "__main__":
    txt = input(txt)
    text_analyser(txt)
 
print(text_analyser(txt))

# ----------------ou------------
mport string

import sys

 

def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """

    if args is None or len(args) == 0:
        args = input("What is the text to analyze? ")

    else:
        args = args[0]

    if type(args) != str:
        print("AssertionError: argument is not a string")
        return

    count_upper = sum(1 for char in args if char.isupper())
    count_lower = sum(1 for char in args if char.islower())
    count_punctuation = sum(1 for char in args if char in string.punctuation)
    count_spaces = sum(1 for char in args if char.isspace())

    print("The text contains " + str(len(args)) + " character(s):")
    print("- " + str(count_upper) + " upper letter(s)")
    print("- " + str(count_lower) + " lower letter(s)")
    print("- " + str(count_punctuation) + " punctuation mark(s)")
    print("- " + str(count_spaces) + " space(s)")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: invalid args count!")
        exit(1)
    text_analyzer(sys.argv[1])




