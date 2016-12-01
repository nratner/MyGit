import urllib
from BeautifulSoup import *

URL = raw_input("Enter the URL:") #Put insurance
link_line = int(raw_input("Enter the line of the desired link:")) - 1 #Put insurance
count = int(raw_input("Enter the loop repeat times:")) #Put insurance

while count >= 0:
    html = urllib.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print URL
    URL = tags[link_line].get("href", None)
    count = count - 1