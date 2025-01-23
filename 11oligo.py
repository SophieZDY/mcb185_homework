#function that returns oligo melting temp given number of ACGT
def tm(a, t, c, g):
    if a+t+c+g <=13:
        Tm = (a+t)*2 + (g+c)*4
    else: Tm = 64.9 + 41*(g+c-16.4) / (a+t+g+c)
    return Tm
print(tm(5,7,3,4))