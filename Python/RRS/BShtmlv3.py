fname = raw_input("Enter file name: ")
fhtml = open(fname)
content = fhtml.read
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'html.parser')
for tag in soup.findall(True):
    if tag.name not in VALID_TAGS:
        tag.extract()
        soup.renderContents()

print(soup)