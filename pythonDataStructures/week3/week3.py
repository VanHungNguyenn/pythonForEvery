# text = open('text.txt')


# count = 0
# for line in text:
#     count += 1

# print(count)

# inp = text.read()
# print(inp)


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Not found file ' + fname)
    quit()

total = 0
num = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line.find(':')
    num += 1
    total += float(line[x+2:])
    
print('Average spam confidence: ' + str(total/num))