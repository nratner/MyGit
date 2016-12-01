# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
total=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    findnumbers = str(tag)
    listnumbers = re.findall('[0-9]+', findnumbers)
    for num in listnumbers:
        num = int(num)
        total = total + num

print total
#     print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
#     print 'Attrs:',tag.attrsimport re
