# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for letters in fh:
    ls = letters.rstrip()
    print(ls.upper())
