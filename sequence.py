#create the first library to include some frequently used functions

#transcription
##convert 'T' to 'U'
##string.replace() return the modified copy
def transcribe(dna):
    return dna.replace('T', 'U')

#function that make reverse-complement strand
def revcomp(dna):
    rc = [] #empty list to hold new sequence
    for nt in dna[::-1]: #read current sequence backward
        if   nt == 'A': rc.append('T')
        elif nt == 'C': rc.append('G')
        elif nt == 'G': rc.append('C')
        elif nt == 'T': rc.append('A')
        else:           rc.append('N') #N for unknown nt (not ACGT)
    return ''.join(rc) #return a string version of list rc

#translation
def translate(dna):
    aas = []
    for i in range(0, len(dna), 3): #steps through indices by 3
        codon = dna[i:i+3] #retrieve codon by stepping through nt sequence 3 letters at a time
        #convert codon to AA
        #right now only recognize start and stop codons and convert everything else to 'X'
        if   codon == 'ATG': aas.append('M')
        elif codon == 'TAA': aas.append('*')
        elif codon == 'TAG': aas.append('*')
        elif codon == 'TGA': aas.append('*')
        else:                aas.append('X')
    return ''.join(aas)

##alternative version to write translation function
'''
def translate(dna):
    codons = ('ATG', 'TAA', 'TAG', 'TGA')
    aminos = 'M***' #M for ATG, * for the rest
    aas = []
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon in codons: #only work for start and end codon
            idx = codons.index(codon) #find index of this codon
            aa = aminos[idx] #find corresponding AA from string aminos
            aas.append(aa) #add this AA to list
            #above three lines can be written as one line; not necesary
            #aas.append(aminos[codons.index(codon)])
        else: #if not start and end codon, convert to 'X'
            aas.append('X')
    return ''.join(aas)
'''