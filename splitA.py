fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid file name:', fname)
    quit()
lst = list()
spline = list()
for line in fh:
    stline = line.rstrip()
    spline = stline.split()
    for nl in spline:
        if nl in lst:
            continue
        else:
            lst.append(nl)
lst.sort()
print(lst)
