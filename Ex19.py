#  In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
#  The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
#  the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#  data url http://py4e-data.dr-chuck.net/comments_1608191.json

import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL- ")
print("Retrieving... ", url)
html = urllib.request.urlopen(url).read()
info = json.loads(html)

sum = 0
many = 0
for value in info["comments"]:
    many = many + 1
    counts = value["count"]
    sum = sum + counts
print("Count: ", many)
print("Sum: ", sum)
