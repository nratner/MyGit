import urllib
from bs4 import BeautifulSoup
import csv

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "badhtmlsubset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")



#this almost works.  Repeats same text over and over
i=1
for stuff in soup.findAll(text="Equipment ID:"):
    print "Count=", i
    equipid = soup.find(text="Equipment ID:").findNext('td')
    location = soup.find(text="Location:").findNext('td')
    inspector = soup.find(text="Inspector:").findNext('td')
    body = soup.find(text="Comments:").findNext('td')
    print "Equipment ID:", equipid.text,"Location:", location.text,"Inspector:", inspector.text
    # print "Location:", location.text
#     print "Inspector", inspector.text
    print "Comments:", body.text
    i = i + 1

