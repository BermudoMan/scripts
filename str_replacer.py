import glob

for file in glob.glob("*.inp"):
    with open(file, 'r') as f:
        old_data = f.read()

        str_old = 'AMPLGROUP=C2v,100, 0.,1.2, 1.2,1.8, 1.8,3.2, 2.6,3.2, 3.2,4., 4.,5.4, 5.4,6.7, 6.7,8., 8.,10., 10.,11.3, 11.3,20.'
        str_new = 'AMPLGROUP=C2v,100, 0.,1.2, 1.2,1.8, 1.8,2.6, 2.6,3.2, 3.2,4., 4.,5.4, 5.4,6.7, 6.7,8., 8.,10., 10.,11.3, 11.3,20.'

        new_data = old_data.replace(str_old, str_new)

    with open(file, 'w') as f:
        f.write(new_data)
