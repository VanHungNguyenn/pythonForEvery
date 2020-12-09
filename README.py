# PYTHON BASIC

jjj = { 'Hung': 23, 'Trong': 28, 'Hiep': 21}
print(list(jjj))
# ['Hung', 'Trong', 'Hiep']
print(jjj.keys())
# ['Hung', 'Trong', 'Hiep']
print(jjj.values())
# [23, 28, 21]
print(jjj.items())
# [('Hung', 23), ('Trong', 28), ('Hiep', 21)]

for i,j in jjj.items():
    print(i,j)


import re   #regex