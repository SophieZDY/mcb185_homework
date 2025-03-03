#program that predicts which protein in a proteome are transmembrane
#8 aa hydrophobic with average KD >= 2.5 in first 30 aa
#and 11 aa hydrophobic with average KD >= 2.0 after first 30 aa
import sys
import mcb185

amino = 'IVLFCMAGTSWYHEQDNKR' #no proline because of alpha-helix structure
score = [4.5,4.2,3.8,2.8,2.5,1.9,1.8,-0.4,-0.7,-0.8,-0.9,-1.3,-3.2,-3.5,-3.5,-3.5,-3.5,-3.9,-4.5] #corresponding hydropathy score of those hydrophobic aa

def is_tmp(seq,w,KD):
    for i in range(len(seq)-w+1):
        s = seq[i:i + w]
        sum = 0
        for aa in s:
            if aa == 'P': break #we are not expected to see proline in transmembrane regions
            sum += score[amino.find(aa)]

        avg = sum / w
        if avg >= KD: return True
    return False


for defline, seq in mcb185.read_fasta(sys.argv[1]):
        signal = is_tmp(seq[:30],8,2.5)
        #tm_region = True
        tm_region = is_tmp(seq[30:],11,2.0)
        if (signal == True) and (tm_region == True):
            print(defline)


'''
2 windows:
w1=8
w2=11
calculate the KD

'''