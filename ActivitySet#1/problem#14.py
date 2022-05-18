# Using Web Services
# https://www.py4e.com/lessons/servces

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL:" )
xml = urlopen(url, context=ctx)

print("retrieving", url)
data = xml.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
results = tree.findall("comments/comment")

total = 0
for i in results:
    number = int(i.find('count').text)
    total = total + number

print(total)