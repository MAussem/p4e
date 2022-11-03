# Use the file name mbox-short.txt as the file name
ct = 0
fnumb = 0
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Invalid file name:', fname)
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        ct = ct + 1
        numb = line.find("0")
        snumb = line[numb:]
        fnumb = fnumb + float(snumb)
    av = fnumb/ct
print("Average spam confidence:", av)
