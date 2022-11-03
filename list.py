#friends = ["B", "GL", "Geo"]
# for i in range(len(friends)):
#    friend = friends[i]
#    print("Merry Christmas", friend)

#numlist = list()
# while True:
#    inp = input("Enter a number: ")
#    if inp == "done":
#        break
#    value = float(inp)
#    numlist.append(value)
#av = sum(numlist) / len(numlist)
#print("Average: ", av)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])
