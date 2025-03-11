#program that reports putative coding genes
'''
Input: FASTA file
Output: GFF of gene features
Parameters: FASTA file, minimum ORF length (e.g. 300 nt including stop)
'''
import sys
import mcb185
length = int(sys.argv[2])

def find_orfs(seq, start_id, frame, strand):
    id = start_id
    pro = mcb185.translate(seq)
    pos = 0

    while pro.find('M') != -1:
        beg = pro.find('M')
        s = pro[beg:]

        if s.find('*') == -1: break
        stop = s.find('*')
        end = beg + stop

        start_pos = pos + beg*3 + frame + 1 #+1 because the coordinate start with 1
        end_pos = pos + end*3 + frame + 1

        if stop*3 >= length:
            orf = pro[beg:end]

            print(f'{name}\t'
                  f'genefinder\t'
                  f'CDS\t'
                  f'{start_pos}\t'
                  f'{end_pos}\t'
                  f'.\t'
                  f'{strand}\t'
                  f'{frame}\t'
                  f'prot-{id}')
            #print(orf)
            id += 1

        pro = pro[end+1:]
        pos += (end+1) * 3
    return id

orf_id = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    description = defline.split()
    name = '>'+description[0]
    genome_size = len(seq)

    rs = mcb185.anti_seq(seq)

    for i in range(3):
        f_seq = seq[i:]
        #f_pro = mcb185.translate(seq[i:])
        #print(seq[i:])
        orf_id = find_orfs(f_seq, orf_id, i, '+')

        r_seq = rs[i:]
        #r_pro = mcb185.translate(rs[i:])
        #print(rs[i:])
        orf_id = find_orfs(r_seq, orf_id, i, '-')