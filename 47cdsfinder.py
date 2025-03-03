#program that finds open reading frame in the E.coli genome
'''
Output: multi-FASTA file of proteins
Must perform a six-frame translation
Proteins must be at least 100 amino acids long
Proteins must start with 'M' and end with '*'
Deflines must have unique identifiers
'''
import sys
import mcb185
import sequence

size = int(sys.argv[2])
sequences = []
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    description = defline.split()
    name = '>'+description[0]
    sequences.append(seq)
genome = ''.join(sequences)

def find_orfs(pro, start_id):
    id = start_id
    while pro.find('M') != -1:
        beg = pro.find('M')
        s = pro[beg:]
        if s.find('*') == -1: break
        stop = s.find('*')
        end = beg + stop
        if stop >= size:
            orf = pro[beg:end]
            print(f'{name}-prot-{id}\n'
                  f'{orf}')
            id += 1
        pro = pro[end:]
    return id

orf_id = 0
#+1, +2, +3 reading frame
for i in range(3):
    forward_pro = mcb185.translate(genome[i:])
    orf_id += find_orfs(forward_pro,orf_id)

#-1, -2, -3 reading frame
rc = sequence.revcomp(genome)
for j in range(3):
    reverse_pro = mcb185.translate(rc[j:])
    orf_id += find_orfs(reverse_pro,orf_id)