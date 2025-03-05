#command line way: gunzip -c ecoli.gff.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -nr
import gzip
import sys

count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line.startswith('#'): continue #function that work as line[0]
        f = line.split()
        feature = f[2]
        if feature not in count: count[feature] = 0 #create key in dict if it's not in dict yet before start counting
        count[feature] += 1
for f, n in count.items(): print(f, n)


