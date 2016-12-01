from bs4 import BeautifulSoup

fhand = raw_input("Enter file name: ")
html = open(fhand).read()
with open(html) as markup:
    soup = BeautifulSoup(markup.read(), "lxml")

file = open(fhand.txt, "w")
    
with open(file, "w") as f:
    f.write(soup.get_text())
    