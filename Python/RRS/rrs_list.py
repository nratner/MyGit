import urllib
from bs4 import BeautifulSoup

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "badhtmlsubset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

lst = list()
for stuff in soup:
    equipids = soup.find(text="Equipment ID:").findNext('td').text
#     location = soup.find(text="Location:").findNext('td')
#     inspector = soup.find(text="Inspector:").findNext('td')
#     body = soup.find(text="Comments:").findNext('td')
    for equipid in stuff:
        if equipid in lst:
            continue
        else:
            lst.append(equipid)

print lst

    #print "Equipment ID:", stuff.findNext('td').text,
    #print "Location", stuff.find(text="Location:").findNext('td')   <--Traceback TypeError: find() takes no keyword arguments

#.findAll(text="Equipment ID:"