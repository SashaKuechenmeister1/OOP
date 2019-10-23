from fractions import Fraction

def GCD(bigger,smaller):
    """this function takes 2 integers and returns the GCD"""
    while smaller != 0:
        (bigger, smaller) = (smaller, bigger % smaller)
    return bigger

def LCM(first,second):
    """this function takes 2 integers and returns the LCM"""

    return first * second / GCD (first,second)

    return LCM

def addFrac(frac1num,frac1den,frac2num,frac2den):
    """this function adds two fractions and returns the sum"""

    return Fraction(frac1num,frac1den) + Fraction(frac2num,frac2den)

def subFrac(frac1num,frac1den,frac2num,frac2den):
    """this function subtracts two fractions and returns the result"""

    return Fraction(frac1num,frac1den) - Fraction(frac2num,frac2den)

def reduceFrac(fracNum,fracDen):
    """this function reduces a fraction and return its simplest form"""

    return Fraction(fracNum,fracDen)



#Main Program

#reads in users input for GCD function
GCD1 = int(input("enter value for 1st gcd num: "))
GCD2 = int(input("enter a value for the 2nd gcd num: "))

#displays the GCD outcome
print("the gcd of", GCD1 , "and", GCD2 , "is: ", GCD(GCD1,GCD2))

#reads in users input for LCM function

LCM1 = int(input("enter a value for 1st lcm num: "))
LCM2 = int(input("enter a value for the 2nd lcm num: "))

#displays the LCM outcome
print("the LCM of", LCM1 , "and", LCM2 , "is: ", LCM (LCM1,LCM2))

#reads in user input for add fracs
n1 = int(input("enter frac1 numerator:"))
n2 = int(input("enter frac1 denominator:"))
n3 = int(input("enter frac2 numerator:"))
n4 = int(input("enter frac2 denominator:"))

#displays the add frac sum
print("the outcome of (", n1,",",n2 , ") and (", n3,",",n4 , ") is: ", addFrac(n1,n2,n3,n4) )

#reads in user input for sub fracs
m1 = int(input("enter frac1 numerator:"))
m2 = int(input("enter frac1 denominator:"))
m3 = int(input("enter frac2 numerator:"))
m4 = int(input("enter frac2 denominator:"))

#displays the sub frac sum
print("the outcome of (", m1,",",m2 , ") and (", 3,",",m4 , ") is: ", subFrac(m1,m2,m3,m4) )

#reads in user input for reducing a fraction to its simplest form
Num = int(input("enter a Numerator"))
Den = int(input("enter a Denominator"))

#displays the simplest form of the fraction
print("The simplest form of (", Num, ",", Den,") is: ", reduceFrac(Num,Den))
