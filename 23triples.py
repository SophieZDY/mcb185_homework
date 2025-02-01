#program that finds all pythagorean triples for triangles with sides a and b less than 100
#all sides including the hypotenuse muse be integers
#check integer: if c%1==0
import math

def triples():
    for a in range(1, 100):
        for b in range(1, 100):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0:
                print(a, b, int(c))
                
triples()

#are we counting 3, 4, 5 and 4, 3, 5 as two separate results?