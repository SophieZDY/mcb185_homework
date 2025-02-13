#30demo.py by Sophie Zhang
#unit3 containers

#strings - immutable
s = 'hello world'
print(s)
##put double quotes inside single quotes or single quotes inside double quotes
s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)
##or backslash the quote to tell python you aren't using it as delimiter
print('hey "dude" don\'t tell me what to do')

##string operation
### + concatenation
### * repetition
### </> comparison compare by their ASCII values

##string methods
print(s.upper()) #make string s all upper case
print(s) #not change the original string (immutable)
print(s.replace('o', ''))
print(s.replace('o','').replace('r', 'i')) #add more to do multiple replacement
print(s.rstrip()) #strip character from the right(space by default)
import math
##f-string - anything in curly brackets is interpolated; code inside curly brackets is live
###inside the {}: f for fixed point; e for exponent notation; <^> for left, center or right justify
print(f'{math.pi}')
print(f'{math.pi:.3f}') #3 fixed digits after decimal
print(f'{1e6 * math.pi:e}') #exponent notation
print(f'{"hello world":>20}') #right justify with space filler
print(f'{"hello world":.>20}') #right justify with dot filler
print(f'{20:<10}{10}') #left justify
##other form, but f-string is the best
print('{} {:.3f}'.format('str.format', math.pi)) #str.format() style
print('%s %.3f' % ('printf', math.pi)) #printf style

#indexes
seq = 'GAATTC'
print(seq[0], seq[1]) #index start with 0
print(seq[-1]) #negative index to count backwards
for nt in seq:
    print(nt, end='') #set end of each print(nt) to be no space, otherwise by default create in new line
print() #create a empty new line

for i in range(len(seq)):
    print(i, seq[i])

#slice - subset of a container
s = 'ABCDEFGHIJ'
print(s[0:5]) #work a little lik range(); 5 is end-before limit
print(s[0:8:2]) #slices can also have a step size; nu default is assumed to be 1
print(s[0:5], s[:5]) #both ABCDE
print(s[5:len(s)], s[5:]) #both FGHIJ
print(s, s[::], s[::1], s[::-1]) #last one print DNA string backward

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(i, codon)

#tuples - immutable
tax = ('Homo', 'sapiens', 9606) #construct tuple
print(tax) #output tuple is written in (), with comma-separated values
##tuples are linear containers of values, so it can be indexed and sliced
print(tax[0]) #put index, return element in that index
print(tax[::-1]) #slice

#enumerate() and zip()
##enumerate() - index and value
###we can use range() to include both indices and values
nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
###tidier alternative: have enumerate() provide you a tuple containing the index and value in separated named variables
for i, nt in enumerate(nts):
    print(i, nt)

##zip() - retrieve element from each container(ie. tuple)
###use range() to simultaneously index separate container
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
###tidier alternative: use zip() to retrieve an element from each container and return them to you in a tuple
for nt, name in zip(nts, names):
    print(nt, name)
###you can even enumerate the zip as shown below; need to unpack the tuple in series using additional parentheses
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

#list
##construct with square brackets and their contents are mutable
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G' #change C to G
print(nts)
##add element to the end of list
nts.append('C')
print(nts)
##remove element from end of list
last = nts.pop()
print(last)
##sort list; you can sort mixture of ints and floats, but can't mix them with strings
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
nucleotides = nts #we just assign a new name to existing list
nucleotides.append('C') #we actually modify both nucleotides and nts
nucleotides.sort()
print(nts, nucleotides) #if you make a new variable to an existing list, is't not a copy
##to make a copy, "shallow" copy - multi-dimensional lists and other complex data structure are not fully copied
nuc = nts.copy()
nuc.pop()
print(nuc, nts) #modify nuc only, while keep nts the same

##create empty list
items = list() #list() with no argument create empty list
print(items)
items.append('eggs')
print(items)

stuff = [] #empty square brackets also create empty list
stuff.append(3)
print(stuff)

##list()
alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph) #list() coerces other 'iterables' into lists
print(aas) #in this case, we convert a string into a list of letters

##split() and join()
###split() - split strings into lists of string; useful for segmenting words
text = 'good day    to you' #delimiter by default is any number of space
words = text.split()
print(words)

line = '1.41, 2.72, 3.14' #for tsv or csv data, split on \t or comma
print(line.split(','))

###join() - join items in list into string with a delimiter; delimiter can be nothing
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#searching
##keyword: in
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

##keyword: index()
print('index G?', alph.index('G')) #return index of the first element it finds
#print('index Z', alph.index('Z')) #error if can't find a matching item

##keyword: find() - very useful behavior only works for strings, not tuples or list
print('find G?', alph.find('G')) #return index of the first element it finds
print('find Z', alph.find('Z')) #return -1 if it can't be found
#if you are searching a list or tuple, and you don't know if the element is in the list, first use in
#if thing in list: idx = list.index(thing)

#practice problems
##function that returns the minimum of a list
'''
def minimum(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min
'''
def minimum(vals):
    min = vals[0]
    for val in vals[1:]:
        if val < min: min = val
    return min

ls = [2, 4, 2, -1, 1, 3]
#print(minimum(ls))

##function that returns both the minimum and maximum values of a list
def extreme(ls):
    min = ls[0]
    max = ls[0]
    for val in ls[1:]:
        if val < min: min = val
        if val > max: max = val
    return min, max
#print(extreme(ls))

##function that returns the mean of the values in a list
def mean(vals):
    sum = 0
    for val in vals:
        sum += val
    mean = sum / len(vals)
    return mean
#print(mean(ls)) #1.83333

##function that computes the entropy of a probability distribution
import math
def entropy(prob):
    h = 0
    for p in prob:
        if p != 0: h -= p * math.log2(p)
    return h
prob = [0.2, 0.3, 0.4, 0.1, 0]
print(entropy(prob))

##function that computes the Kullback-Leibler distance between two sets of probability distributions
def kldistance(prob1, prob2):
    dist = 0
    for p1, p2 in zip(prob1, prob2):
        if p2 != 0 and p1 != 0: dist += p1 * math.log2(p1 / p2)
    return dist
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2]
#print(kldistance(p1, p2))
#"correct version"
def dkl(P, Q):
     d = 0
     for p, q in zip(P, Q):
        d += p * math.log2(p/q)
     return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2) #ok to use list or tuple because both can be zipped in parallel
#print(dkl(p1, p2))

#command line data
##sys.argv - complete list of words on command line (argv for argument vector
import sys
print(sys.argv)
#print(sys.argv[0]) #return name of your program
#sys.argv[1] is the next stuff in list, if you have any (i.e. put in command line)

##converting types
i = int('42')
x = float('0.61803')
#x = float('hello') #we could not convert string to float or int
print(i * x)

#pairwise comparison
'''
for i in range(0, len(list)):
    for j in range(X, len(list)):
        (coding)
X = 0: all combination
X = i: half-matrix with diagonal
X = i+1: half-matrix without diagonal
'''