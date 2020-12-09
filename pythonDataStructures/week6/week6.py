name = input("Enter file:")
try:
    handle = open(name)
except:
    print("Not file")
    quit()

print(handle)

x = dict()

for line in handle:
    word = line.rstrip()
    if word.startswith('From '):
        x[word.split()[5].split(':')[0]] = x.get(word.split()[5].split(':')[0],0) + 1

x = (sorted([(k,v) for k,v in x.items()]))

for k,v in x:
    print(k,v)
