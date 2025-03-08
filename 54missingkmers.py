#program that searches sequences for the smallest missing k-mer
import sys
import mcb185
import itertools
def kmers(k):
    kmers = {}
    for nts in itertools.product('ACGT', repeat=k): #itertools.product() to generate all possible kmers
        kmer = ''.join(nts)
        kmers[kmer] = 0
    return kmers

k = 0 #kmer size
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    rs = mcb185.anti_seq(seq)
    while True:
        k += 1
        counts = kmers(k)
        for j in range(len(seq) -k +1):
            kmer1 = seq[j:j+k]
            counts[kmer1] += 1
            kmer2 = rs[j:j+k]
            counts[kmer2] += 1
        #print(counts)
        missing_kmer = 0
        for kmer, n in counts.items():
            if n == 0:
                missing_kmer += 1
                #print(kmer)
        if missing_kmer != 0:
            print(f'k={k}, missing kmers={missing_kmer}')
            break