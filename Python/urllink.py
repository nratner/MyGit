# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
links = list()
x = 4
# Retrieve all of the anchor tags
while x > 0:
   site = urllib.urlopen(url).read()
   soup2 = BeautifulSoup(html2)
   tags = soup('a')
   for tag in 
tags = soup('a')
for tag in tags:
    print tag.get('href', None)