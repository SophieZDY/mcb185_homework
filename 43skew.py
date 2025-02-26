import sequence
seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10 #window with size of 10
for i in range(len(seq) -w +1): #canoical window
    s = seq[i:i+w]
    print(i, sequence.gc_comp(s),sequence.gc_skew(s))