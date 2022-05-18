#Using web services 2
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file

from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
js = urlopen(url, context=ctx)
data = js.read()
info = json.loads(data)

total = 0
for i in range(len(info["comments"])):
    total = total + int(info["comments"][i]["count"])

print(total)
