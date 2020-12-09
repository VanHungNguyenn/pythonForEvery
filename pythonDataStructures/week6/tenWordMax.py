f = open(input("Input file: "))
counts = dict()
for line in f:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Option 1
lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)

lst.sort(lst, reverse=True)

for v,k in lst[:10]:
    print(k,v)


# #Option 2
# c = {'a': 10, 'b': 1, 'c': 5}
# print(sorted([(v,k) for k,v in c.items()]))