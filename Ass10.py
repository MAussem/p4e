name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
c = dict()

for line in handle:
    if line.startswith("From "):
        time = line.split()[5].split(":")
        c[time[0]] = c.get(time[0], 0) + 1

lst = list()

for key, value in c.items():
    lst.append((key, value))
lst.sort()

for hour, counts in lst:
    print(hour, counts)
