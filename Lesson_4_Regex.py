# 1. Python Regular Expressions Mastery


# Task 1: Name Verification



# Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

# Use the following list as an argument to test your function.



names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


# Expected Outcome:

# Abraham Lincoln
# Andrew P Garfield
# Invalid name
# Connor Milliken
# Jordan Alexander Williams
# Invalid name
# Invalid name


import re

def verify_names(names):

    pattern = re.compile(r'^[A-Z][a-z]+(?: [A-Z][a-z]*)+$')
    
    for name in names:
        if pattern.match(name):
            print(name)
        else:
            print("Invalid name")


verify_names(names)