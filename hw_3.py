# Name: Seungah Ha
# hw3.py

##### Template for Homework 3, exercises 1 -  ######

from math import *
import random

# ********** Exercise 1 ********** 

# Define is_divisible function here

def is_divisible(a,b):
    if b!=0:
        if a%b==0:
            print 'true'
        else:
            print 'false'
    if b==0:
        print 'infinity'

# ********** Exercise 2 ********** 

# Define not_equal function here

def not_equal(a,b):
    if a-b==0:
        print 'equal'
    else:
        print 'not equal'
               
# Test cases for not_equal
not_equal(5,4) # not equal
not_equal(3,3) # equal

# ********** Exercise 3 ********** 

## 1 - multadd function
def multadd(a,b,c):
    return a*b+c

## 2 - Equations
angle_test = multadd(0.5, cos(pi/4), sin(pi/4))
ceiling_test = multadd(2, log(12,7), ceil(276/19))


# Test Cases
angle_test = multadd(0.5, cos(pi/4), sin(pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multadd(2, log(12,7), ceil(276/19))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    n = random.randint(0,100)
    if n%3==0:
        print ('For random number', n, 'the result is: True')
    else: 
        print ('For random number', n, 'the result is: False')

        
# Test Cases
rand_divis_3()
rand_divis_3()

