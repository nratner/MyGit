import urllib
from bs4 import BeautifulSoup

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "badhtmlsubset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

i = 1
for stuff in soup.findAll('td'):
    print i
    print "Equipment ID:", stuff.find(text="Equipment ID:").text
    i = i + 1
    #print "Location", stuff.find(text="Location:").findNext('td')   <--Traceback TypeError: find() takes no keyword arguments

