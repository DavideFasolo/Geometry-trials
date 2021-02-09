from Classes import *

import random as ra

def random_fraction_str():
    return str(round(ma.sqrt(ra.randint(0,10000)/ra.randint(0,10000)),3))+"/"+str(round(ma.sqrt(ra.randint(1,10000)/ra.randint(1,10000)),3))

def random_float_str():
    return 4

print(random_fraction_str())
pippo=Punto(12,random_fraction_str(),6.2)
print(pippo.y)