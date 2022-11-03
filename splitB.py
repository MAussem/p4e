fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('Invalid file name:', fname)
    quit()
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    stline = line.rstrip()
    words = stline.split()
    print(words[1])
    count = count+1
print("There were", count, "lines in the file with From as the first word")
