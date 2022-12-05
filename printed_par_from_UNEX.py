import subprocess
import glob
from itertools import islice

word = 'Distance'
word2 = 'Angle('
word3 = 'Torsion('
sum = open('sum.txt', 'w+')

for file in glob.glob("*.ks"):
    sum.write(file + 2*'\n')
    i = open(file, 'r')
    for j in iter(i):
        if word in j:
            y = j.find("r_c=")
            z = j[y+4:y+14] + '\n'
            sum.write(z)
        elif word2 in j:
            y = j.find(':')
            z = j[y + 2:y + 15] + '\n'
            sum.write(z)
        elif word3 in j:
            y = j.find(':')
            z = j[y + 2:y + 15] + '\n'
            sum.write(z)
    i.close()
sum.close()

