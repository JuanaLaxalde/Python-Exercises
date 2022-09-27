#  In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
#  The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
#  scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat 
#  the process a number of times and report the last name you find.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
# SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    y = str(tag)
    x = re.findall("[0-9]+", y)
    for i in x:
        i = int(i)
        sum = sum + i
        count = count + 1
print("Count", count)
print(sum)
