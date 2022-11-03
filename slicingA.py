str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(":")
sppos = str.find("5", atpos)
final = str[atpos+1: sppos+1]
final_fl = float(final)
print(final_fl)
