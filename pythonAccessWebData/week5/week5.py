import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter location: ')
print('Retrieving: ', address)
html = urllib.request.urlopen(address).read()
stuff = ET.fromstring(html)

# print(stuff)

lst = stuff.findall('comments/comment')

total = 0

for item in lst:
    number = item.find('count').text
    total += int(number)

print(total)