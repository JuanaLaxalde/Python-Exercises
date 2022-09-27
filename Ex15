#  In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
#  The program will use urllib to read the HTML from the data files below, and parse the data, extracting 
#  numbers and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import bs4
url = input("Enter URL - ")
html = urllib.request.urlopen(url).read()
soup = bs4(html, 'html.parser')
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
