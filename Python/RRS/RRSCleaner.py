fname = raw_input("Enter file name: ")
fhtml = open(fname)
content = fhtml.read
from bs4 import BeautifulSoup

soup = BeautifulSoup(content)
text = soup.get_text()
print(text)