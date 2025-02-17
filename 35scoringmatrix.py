#program that can print out a match-mismatch scoring matrix

import sys
sequence = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])

#sequence = "ACGT"
#match = 1
#mismatch = -1

#print first row, the nucleotide in a row
for nuc in sequence:
    print('\t',end=' ')
    print(nuc,end=' ')

for nuc1 in sequence:
    print('\n',nuc1,end='\t')
    for nuc2 in sequence:
        if nuc1 == nuc2: print('+1',end='\t')
        else: print('-1',end='\t')