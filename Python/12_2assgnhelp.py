import urllib
from bs4 import BeautifulSoup

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