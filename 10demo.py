# 10demo.py by Sophie Zhang

import math

print ("hello, again") #greeting
"""
This is a 
multi-line comment
"""
"""
#math
print(1.5e-2)
print(1+1)
print(1-1)
print(2*2)
print(1/2)
print(2**3) #power, or exponentiation
print(5//2) #utput is integer divide
print(5%2) #remainder, 5 mod 2
print(5*(2+1)) #precedence
##math function
print(abs(-1)) #absolute value of -1
print(pow(2,3)) #2 to the power of 3
print(math.pow(2,3))
print(round(2.333333,ndigits=3)) #round off some value to n digits
print(math.log(2)) #log in base e
print(math.sqrt(2)) #sqrt root; math.sqrt will return a float number
#math.inf; math.nan
"""
print(0.1 * 1)
print(0.1 * 3)#can't get exact 0.3 b/c 0.1 can't be represented exactly by IEEE754 standard for storing 8-byte floats

#variable
a = 3 #side of triangle
b = 4 #side of triangle
c = math.sqrt(a**2 + b**2) #hypotenuse
print (c)
print(type(a), type(b), type(c), sep=',', end='!\n')

#function - reusable code constructs that form the backbone of computer programs
def pythagoras(a, b): #a, b works as parameters of the function
    c = math.sqrt(a**2 + b**2)
    return c #this function is also an example of block structure
hyp = pythagoras(3,4)
print(hyp)
#simplified version:
#def pythagoras(a, b):
#   return math.sqrt(a**2 + b**2)
#print(pythagoras(3, 4))
#if there is only 1 statement in a block, we may omit the indentation
def pyth(a,b): return math.sqrt(a**2 + b**2) #only work if we have one statement

#practice
def circle_area(r): return math.pi * r**2
def circle_circumferences(r): return 2 * math.pi * r
def sphere_volume(r): return 4/3 * math.pi * pow(r,3)
def rec_area(w, h): return w * h
##convert temp from F to C or vice-versa

##convert speed from MPH to KPH or vice-versa

##compute DNA concentration from OD260

##compute the arithmetic mean of 3 numbers

##compute the geometric mean of 3 numbers

##compute the harmonic mean of 3 numbers

##computer the distance between 2 points in a graph

#string
s = 'hello world'
print(s, type(s))
##string comparision is done by comparing their ASCII value; thus "A" < "B", but "B" < "a"
#conditionals
##if
a = 2
b = 2
if a == b: #== for equality
    print('a equals b')
def is_even(x):
    if x % 2 == 0: return True
    return False
print(is_even(2))
print(is_even(3))

##boolean - always return 2 values
c = a == b
print(c, type(c))

##if-elif-else; only the firsst true condition is executed
if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')
###or format as one-liners
if   a < b: print('a < b')
elif a > b: print('a > b')
else:       print('a ==b')

##chaining; boolean expression can be chained with and and or and inverted with not
if a < b or a > b: print('all things being equal, a and bare not')
if a > b and a > b: print('you are living in a strance world')
if not False: print(True)

##floating point warning
###never test for equality with floating point numbers
if math.isclose(a, b): print('close enough')

#practice
def is_integer(a):
	if a % 1 == 0: return print(str(a), 'is an integer')
	return print(str(a), 'is not an integer')
is_integer(2.11)
def is_prob(p):
	if p > 1 or p < 0: return False
	return True
print(is_prob(0.3))
def nt_weight(a):
	if a == 'a' or 'A': return print('molecular weight of A is')
	elif a == 't' or 'T': return print('molecular weight of T is')
	elif a == 'g' or 'G': return print('moelcular weight of G is')
	elif a == 'c' or 'C': return print('molecular weight of C is')
	else: return None
def dna_complement(x):
	if x == 'a' or x == 'A': return 'T'
	elif x == 't' or x == 'T': return 'A'
	elif x == 'g' or x == 'G': return 'C'
	elif x == 'c' or x == 'C': return 'G'
	else: return None
print(dna_complement('c'))
#more practice
def max_num(x, y, z):
	if x >= y and x >= z: return x
	elif y >= x and y >= z: return y
	else: return z
print(max_num(6,3,11))
def table(a, b, c, d):
	return
def nt_entropy(a, t, c, g):
	return
