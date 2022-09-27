#  Retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#  http://data.pr4e.org/intro-short.txt


import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
headers = fhand.info()
print(headers)
