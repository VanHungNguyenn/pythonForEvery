import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    0332305444
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Atrr:', tree.find('email').get('hide'))