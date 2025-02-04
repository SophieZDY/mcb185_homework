#program that simulates saving throws against DCs of 5, 10, and 15

import random
def savingthrows(DC): #determine the difficulty class
    throw = random.randint(1, 20) #throw one d20
    if throw >= DC:
        return print(throw, "Success")
    else: return print(throw, "Fail")
savingthrows(5)
savingthrows(10)
savingthrows(15)