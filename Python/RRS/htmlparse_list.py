import urllib
from bs4 import BeautifulSoup

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "linnrrsdbs_subset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")
body = soup.findAll('tbody')

for stuff in body:
    specs = stuff.find_all_next('td')
    prin











# i=1
# for stuff in soup.findAll('tbody'):
#     print "Count=", i
    #print "Equipment ID:", soup.find(text="Equipment ID:").findNext('td').text
    #print "Location:", soup.find(text="Location:").findNext('td').text
    # inspector = soup.find(text="Inspector:").findNext('td')
#     body = soup.find(text="Comments:").findNext('td')
#     print "Equipment ID:", equipid.text,"Location:", location.text,"Inspector:", inspector.text
    #print "Comments:", body.text
    #i = i + 1

