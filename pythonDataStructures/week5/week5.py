name = input("Enter file:")
try:
    handle = open(name)
except:
    print("Not file")
    quit()

x = dict()

for line in handle:
    word = line.rstrip()
    if word.startswith('From '):
        x[word.split()[1]] = x.get(word.split()[1],0) + 1
        
bigMail = None
bigCount = None
for mail,count in x.items():
    if bigCount is None or count > bigCount:
        bigMail = mail
        bigCount = count

print(bigMail, bigCount)