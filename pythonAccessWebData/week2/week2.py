import re

name = open('regex_sum_1078969.txt')

x = list()
for line in name:
    y = re.findall('[0-9]+',line)
    x = x+y

total = 0 
for i in x:
    total += int(i)

print(total)