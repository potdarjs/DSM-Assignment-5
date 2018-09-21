"""
Assignment 5
Data Science Masters

"""
# 1.	Write a function to compute 5/0 and use try/except to catch the exceptions.

import sys

def division(a,b):
    """
    This functions return quotient where
    quotient = dividend ÷ divisor
    """
    try :
        return a/b
    except Exception as e:
        print("\nexception : {}".format(sys.exc_info()[1]))
        sys.exit()

def main():
    a = int(input("Enter dividend : "))
    b = int(input("Enter divisor : "))
    result = division(a,b)
    print("\noutput of {}/{} is {}".format(a,b,result))
    
if __name__  == '__main__':
    main()

# Implement a Python program to generate all sentences where subject is in 
# ["Americans", "Indians"] and verb is in ["Play", "watch"] 
# and the object is in ["Baseball","cricket"].

subjects=["Americans","Indians"] 
verbs=["play","watch"] 
objects=["Baseball","Cricket"]

for subject in subjects :
    for verb in verbs :
        for object in objects :
            print("{} {} {}.".format(subject,verb,object))
            