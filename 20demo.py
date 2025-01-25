#20.demo.py by Sophie Zhang
#unit2 iteration

#tuples - collection of values separted by a comma
t = 1, 2 #this is a tuple
print(t) #print (1, 2)
print(type(t))
#tuple can contain a mixture of types
person = 'Steve', 21, 57891.50 #name, age, yearly income
print(person)
#function can return multiple values by returning a tuple
def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
print(midpoint(1,2,3,4))
m = midpoint(1, 2, 3, 4) #m is a tuple, or a single variable contains 2 separated values
mx, my = midpoint(1, 2, 3, 4) #unpack the tuple; better practice
print(mx, my) #print separate values
print(m[0], m[1]) #each term in tuple gets a numeric index starting at 0

#iteration
##while
###while <boolean expression is True>:
###    do_something
i = 0
"""
while True:
    i += 1
    print('hey', i)
    if i == 3: break #use break statement to break the loop

while i < 3: #better way to break whiile loop by providing some condition
    i += 1
    print('hey', i)
"""
i = 1
while i < 10:
    print(i)
    i += 3
print('final value of i is', i)

##for
for i in range(1, 10, 3): #range function generates integers given an initial value 1, an end-before limit 10, and an increment 3
    print(i)
for i in range(5): #start at 0 by defalut, end-before limit is 5 (end at 4)
    print(i)
###the following do the exact same thing:
###for i in range(5): print(i)
###for i in range(0,5): print(i)
###for i in range(0,5,1): print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)
for i in range(len(basket)):
    print(basket[i])
print(len(basket)) #return number of items in the basket

##nesting
for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd')