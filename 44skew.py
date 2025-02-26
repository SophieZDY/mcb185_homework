import sys
import sequence
import mcb185
#seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
#w = 10
sequences = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    sequences.append(seq)
genome = ''.join(sequences)

w = int(sys.argv[2])
#initial window
s_1 = genome[:w]
print('0', sequence.gc_comp(s_1), sequence.gc_skew(s_1))

c = s_1.count('C') #number of c in initial window
g = s_1.count('G')

for i in range(1,len(genome) -w +1):
    remove = genome[i-1]
    add = genome[i+w-1]
    if remove == 'C':
        c -= 1
    elif remove == 'G':
        g -= 1

    if add == 'C':
        c += 1
    elif add == 'G':
        g += 1

    gc_comp = (c+g) / w
    if (g + c) == 0: gc_skew = 0
    else: gc_skew = (g-c) / (g+c)
    print(i, gc_comp, gc_skew)

#slow algorithm
'''
sequences = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    sequences.append(seq)
genome = ''.join(sequences)
w = int(sys.argv[2])

for i in range(len(genome) -w +1):
    s = genome[i:i+w]
    print(i, sequence.gc_comp(s), sequence.gc_skew(s))
'''