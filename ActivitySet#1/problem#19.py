#Network Programming 3
#The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter url: ")
pos = int(input("Enter the position: "))
finalval = int(input("enter number of times to loop: "))

for i in range(finalval):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[pos-1].get('href', None)

    e = int(url.find('.', 39))
    name = url[39:e]
   

print(name)

