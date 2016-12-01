from bs4 import BeautifulSoup
markup = open("Linn_site_sample.html")
soup = BeautifulSoup(markup.read(), "lxml")
markup.close()
f = open("Linn_site_sample1.txt", "w")

#soup = BeautifulSoup(html)
#total=0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
#     # Look at the parts of a tag
    findnumbers = str(tag)
    listnumbers = re.findall('ABC', findnumbers)
#    #  for num in listnumbers:
#         num = int(num)
#         total = total + num

# f.write(soup.get_text())
# f.close()

print soup.get_text()
print tags