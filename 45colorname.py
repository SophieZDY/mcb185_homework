import sys
colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

input_rgb = []
input_rgb.append(R)
input_rgb.append(G)
input_rgb.append(B)

##c80032
def dtc(P,Q):
    d = 0
    for p,q in zip(P,Q):
        d += abs(int(p)-int(q))
    return d
min = 750
all_d = []
name = []
with open(colorfile) as fp:
    for line in fp:
        lines = line.rstrip()
        f = lines.split('\t')
        name.append(f[0])
        color = f[2].split(',')
        d = dtc(input_rgb,color)
        all_d.append(d)
        if d < min: min = d

index = all_d.index(min)
closest_name = name[index]

print(closest_name)


'''
name = []
r_value = []
g_value = []
b_value = []

fp = open(colorfile)
for line in fp:
    lines = line.rstrip() #get rid of newline character
    words = lines.split('\t') #separte different columns
    name.append(words[0])
    color_value = words[2].split(',') #separate different color values
    r_value.append(color_value[0])
    g_value.append(color_value[1])
    b_value.append(color_value[2])

fp.close()
'''
def dtc(P,Q):
    d = 0
    for p,q in zip(P,Q):
        d += abs(p-q)
    return d