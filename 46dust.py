'''
input: multi-FASTA file of DNA
output: multi-FASTA file of DNA with low complexity regions masked
change all low-complexity regions to 'N' in the output
provide parameter for fasta file, window size, and entropy
'''
import sys
import mcb185
import math
filename = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])
sequences = []
for defline, seq in mcb185.read_fasta(filename):
    sequences.append(seq)
genome = ''.join(sequences)

def entropy(s):
    A = s.count('A')
    C = s.count('C')
    G = s.count('G')
    T = s.count('T')
    probs = [A / w, C / w, G / w, T / w]

    h = 0
    for p in probs:
        if p != 0: h -= p * math.log2(p)
        else: h -= 0
    return h

dust_genome=''
for i in range(len(genome) -w +1):
    s = genome[i:i+w]
    add = genome[i+w-1]

    h = entropy(s)
    if h <= threshold:
        dust_genome = dust_genome[:-w+1] + 'N' * w
    else:
        if i == 0:
            dust_genome += s
        dust_genome += add
    #print(h,dust_genome)
print(f'{defline}\n'
      f'{dust_genome[:180]}')