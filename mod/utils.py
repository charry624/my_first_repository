import math 
import random 

def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi/2)

def mt_elog():
    return math.log(math.e)

def mt_exp(x) : 
    return math.exp(x)

def mt_pi():
    return math.pi 

import random as rd

res = rd.randint(1,100)
print(res)

my_list =["apple", "banana","cherry"]
lres =rd.choice(my_list)
print(lres)

fres = rd.random() 
print(fres)

nvres = rd.normalvariate()
print(nvres)