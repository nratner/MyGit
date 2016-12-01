import urllib
from BeautifulSoup import *

URL = raw_input("Enter the URL:")
linkpos = int(raw_input("Enter the link position:")) - 1
count = int(raw_input("Enter the number of loops:"))

while count >= 0:
    html = urllib.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print URL
    URL = tags[linkpos].get("href", None)
    count = count - 1