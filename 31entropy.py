import sys
import math

#harvest words on command line and turn them into prob.
probs = []
for arg in sys.argv[1:]: #skip first argument, which is the name of program
    f = float(arg)
    if f <= 0 or f >= 1: sys.exit('error: not a probability')
    probs.append(float(arg))

#check if sum of prob. on command line are equal to 1.0 (near 1.0)
total = 0
for p in probs: total += p
if not math.isclose(total, 1.0):
    sys.exit('error: probs must sum to 1.0')

h = 0
for p in probs:
    h -= p * math.log2(p)

print(f'{h:.4f}')

'''
#rewrite

probs = []
for i in sys.argv[1:]:
    f = float(i)
    if f >= 1 or f <= 0:
        sys.exit('error: not prob.')
    else: probs.append(float(i))

sum = 0
for p in probs:
    sum += p
if not math.isclose(sum, 1.0):
    sys.exit('error: sum or prob. must be 1')

h = 0
for i in probs:
    h -= i * math.log2(i)
print(f'{h:.4f}')
'''