import urllib
from bs4 import BeautifulSoup

# This function will get the Nth link object from the given url.
# To be safe you should make sure the nth link exists (I did not)
def getNthLink(url, n):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

url = "http://datascienceglossary.org/"