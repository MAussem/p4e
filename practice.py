c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))

# find the 10 most common words in romeo.txt
fhand = input("Enter file name: ")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for value, key in lst[:10]:
    print(key, value)
