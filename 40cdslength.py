import gzip
import sys
#select specific line to process
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#': #skip over comment line
            words = line.split()
            if words[2] == 'CDS': #find CDS features (or skip over all non-CDS feature)
                beg = int(words[3]) #extract begin and end coordinates; convert to integers
                end = int(words[4])
                print(end - beg + 1) #report length of CDS

#use continue ro get rid of problem cases and operates on what is left
#stylistically, the code that uses continue if preferred
with gzip.open(sys.argv[1],'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)
