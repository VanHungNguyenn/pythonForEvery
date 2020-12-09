import ssl
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('span')
total = 0
for tag in tags:
   # Look at the parts of a tag
   total += int(tag.contents[0])
print(total)

