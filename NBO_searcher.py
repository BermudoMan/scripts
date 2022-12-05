import glob
from itertools import islice

start = ' Second Order Perturbation Theory Analysis of Fock Matrix in NBO Basis'
stop = ' Natural Bond Orbitals (Summary):'


def counter_x():
    for x, value in enumerate(f):
        if start in value:
            return x + 1


def counter_y():
    f.seek(0)
    for y, value in enumerate(f):
        if stop in value:
            return y + 1


words = ['N  14 - N  15', 'N  14 - N  15', 'C   9 - N  14', 'N  15 - C  16', 'LP (   1) N', 'LP (   1) O  22', 'LP (   2) O  22',
         'H  37']

for file in glob.glob("*.log"):
    f = open(file, 'r')
    name = file + '.txt'
    NBO = open(name, "+w")

    sort1 = 'RY'
    sort2 = 'CR'
    NBO.write(file)
    NBO.write(2 * "\n")

    x = counter_x()
    print(x)
    y = counter_y()
    print(y)

    for word in words:
        NBO.write(2 * "\n")
        NBO.write("!!!!!!" + word + "!!!!!!")
        NBO.write(2 * "\n")
        for line in islice(f, x, y):
            if word in line:
                if sort1 not in line and sort2 not in line:
                    NBO.write(line)

        f.seek(0)
    f.close()
    NBO.close()
