import glob

rf = open('fr.txt',"+w")


for file in glob.glob("*.ks"):
    f = open(file, 'r')
    word = 'Total sM(s)'
    for i in iter(f):
        if word in i:
            save = file + '\t' + i[30:38]
    rf.write(save)
    f.close()
rf.close()
