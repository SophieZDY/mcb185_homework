#calculates the composition of nucleotides in a fasta file

import sys
import mcb185
#GC composition
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    gc = 0
    for nt in seq:
        if nt == 'C' or nt == 'G': gc += 1
    print(name, gc/len(seq))
'''
#individual variables, count 5 nucleotides (ACGTN)
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    A = 0
    C = 0
    G = 0
    T = 0
    N = 0
    for nt in seq:
        if nt == 'A': A += 1
        elif nt == 'C': C += 1
        elif nt == 'G': G += 1
        elif nt == 'T': T += 1
        else:           N += 1
    print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))
'''
#list variation - create list to hold the counts
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    counts = [0, 0, 0, 0, 0] # A, C, G, T, N
    for nt in seq:
        if   nt == 'A': counts[0] += 1
        elif nt == 'C': counts[1] += 1
        elif nt == 'G': counts[2] += 1
        elif nt == 'T': counts[3] += 1
        else:           counts[4] += 1
    print(name, end = ' ')
    for n in counts: print(n/len(seq), end = ' ')
    print()
'''
#indexing with str.find()
##replace the if-elif-else with sstr.find()
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    nts = 'ACGTN'
    counts = [0] * len(nts) #create list of five 0s
    for nt in seq:
        idx = nts.find(nt) #find index of nt in nts(ACGTN)
        counts[idx] += 1 #add 1 to corresponding position
    print(name, end = ' ')
    for n in counts: print(n/len(seq), end = ' ')
    print()
'''
#counting any letter - need to make the alphabet container mutable (i.e, a list)
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    #initialized for add whenever a new letter is seen
    nts = []
    counts = []
    for nt in seq:
        if nt not in nts: #if there is a new letter, we add to nts, and increase size of counts by 1 (adding one 0 to list)
            nts.append(nt)
            counts.append(0)
        idx = nts.index(nt) #use nts.index() because we want to locate index of nt in list
        counts[idx] += 1
    print(name)
    for nt, n in zip(nts, counts):
        print(nt, n, n/len(seq))
    print()
'''
#counting with str.count() - to count specific letters
##tidy and efficient, but have to specify the alphabet ahead of time
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    print(name, end = ' ')
    for nt in 'ACGTN':
        print(seq.count(nt) / len(seq), end = ' ')
    print()