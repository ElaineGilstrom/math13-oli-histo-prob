#import statistics
from operator import itemgetter as iGet

def parse(data):
    s = data.split(",")
    r = []
    r.append(int(s[0]))
    r.append(s[1])
    r.append(s[2])
    r.append(int(s[3]))
    return r

def isIn(t, l):
    r = -1
    for i in range(0, len(l)):
        if l[i][0] == t:
            r = i
            break
    return r

def genHisto(binsize, lst):
    lst.sort()
    mini = lst[0]
    maxi = lst[len(lst) - 1]
    rng = maxi - mini
    histo = [[[i, i + binsize], 0] for i in range(mini, maxi + binsize, binsize)]
    li = 0
    for i in lst:
        while i >= histo[li][0][1]:
            li += 1
        histo[li][1] += 1
    return histo


"""
working with a simple grid, and not wanting to use multiple chars per line is
making this a little hard to enterpret. The line the colom on is the lower bound
with the next line being the upper bound for the bin.
"""
def printHisto(histo):
    m = max(histo, key=iGet(1))[1]
    ml = len(str(m))#kinda hackey.. but it'll work
    while m > 0:
        p = str(m)
        if len(p) < ml:
            p += " " * (ml - len(p))#pads out size col
        for i in range(0, len(histo)):
            if histo[i][1] >= m:
                p += "XXX"
            else:
                p += "   "
        print p
        m -= 1
    p = " " * ml
    for i in histo:
        p += str(i[0][0]) + ","
    p += str(histo[len(histo) - 1][0][1])
    print p

data = []

f = open("oscars.csv", "r")

for l in f:
    data.append(parse(l))

f.close()

ages = [i[len(i) - 1] for i in data]

for i in range(2,10):
    print "\n\n"
    print i
    print "\n"
    printHisto(genHisto(i, ages))

"""
sa = []
for i in ages:
    n = isIn(i, sa)
    if n >= 0:
        sa[n][1] += 1
    else:
        sa.append([i, 1])

sa.sort(key=iGet(0))
print sa
"""
