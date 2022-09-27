#  In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#  The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
#  the comment counts from the XML data, compute the sum of the numbers in the file.
#  link to the data http://py4e-data.dr-chuck.net/comments_1608190.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")
print('Retrieving', url)
html = urllib.request.urlopen(url).read()
print("Retrieved", len(html), "characters")

xml = ET.fromstring(html)
lst = xml.findall ("comments/comment")
#print(lst)

sum = 0
count = 0
for value in lst:
    count = count + 1
    v = value.find('count').text
    sum = sum + float(v)
print("Count: ",count)
print("Sum: ",sum)
