import sys
import mcb185
#mcb185.read_fasta() helps to extract definition line(without >) and sequences from fasta file
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))

#each iteration of te for loop retrieves the next record from FASTA file
#each record is returned as a tuple containing the definition line and the sequence