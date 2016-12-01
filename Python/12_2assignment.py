# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup('a')

links = list()
for tag in tags:
    link = getNthLink(url,3)



#x = 4
# Retrieve all of the anchor tags
for tag in tags:
    link = getNthLink(url,3)
    url = tag.get('href')
    while x > 0:
        x = x -1
    print url


# This function will get the Nth link object from the given url.
# To be safe you should make sure the nth link exists (I did not)
def getNthLink(url, n):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[n-1]

url = "http://python-data.dr-chuck.net/known_by_Fikret.html"

# This iterates 4 times, each time grabbing the 3rd link object
# For convenience it prints the url each time.
for i in xrange(4):
    tag = getNthLink(url,3)
    url = tag.get('href')
    print url

# Finally after 4 times we grab the content from the last tag
print tag.contents[0]