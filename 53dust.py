import argparse
import mcb185
import math

#create argument parser object in a variable called parser
parser = argparse.ArgumentParser(description='DNA entropy filter.')
#add different positional argument
parser.add_argument('fasta', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20, help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
parser.add_argument('--wrap', type=int, default=80, help='wrap size [%(default)i]')
arg = parser.parse_args() #create arg object by harvesting the values on command line and assigning them to various properties
##%(default) to advertise the default values in usage statement; s, i, f stands for str, int, and float
#print('dusting with', arg.fasta., arg.size, arg.entropy, arg.lower)

'''
from 46dust.py
input: multi-FASTA file of DNA
output: multi-FASTA file of DNA with low complexity regions masked
change all low-complexity regions to 'N' in the output
provide parameter for fasta file, window size, and entropy
'''
def entropy(k):
    a = k.count('A') / len(k)
    c = k.count('C') / len(k)
    g = k.count('G') / len(k)
    t = k.count('T') / len(k)
    h = 0
    if a != 0: h -= a * math.log2(a)
    if c != 0: h -= c * math.log2(c)
    if g != 0: h -= g * math.log2(g)
    if t != 0: h -= t * math.log2(t)
    return h

sequences = []
for defline, seq in mcb185.read_fasta(arg.fasta):
    print('>',defline, sep= '')

    masked = list(seq) #list version of seq
    for i in range(len(seq) -arg.size +1): #arg.size is the window size we put in command line
        k = seq[i:i+arg.size]
        if entropy(k) < arg.entropy:
            for j in range(i,i+arg.size):
                if arg.lower:
                    masked[j] = seq[j].lower()
                masked[j] = 'N'
    mask = ''.join(masked)
    for i in range(0, len(seq),arg.wrap):
        print(mask[i:i+arg.wrap])
