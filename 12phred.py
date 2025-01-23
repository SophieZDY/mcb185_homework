import math
#function that convert quality value symbol into error rates and vice-versa
def char_to_prob(x): #convert quality value symbols to error rate
    Q = ord(x) - 33
    p = math.pow(10, -Q/10)
    return p
def prob_to_char(x): #convert error rate to character
    Q = -10 * math.log10(x)
    return chr(int(Q+33))
print(char_to_prob('A'))
print(prob_to_char(0.001))