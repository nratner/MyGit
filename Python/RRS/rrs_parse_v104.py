import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
from bs4 import BeautifulSoup
import csv

fname = "linnrrsdbs_subset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

#This code prints out the correct format, but does not print unique information for each loop. Just repeats the same information over and over.
i=1
equipid = soup.findAll(text="Equipment ID:")
location = soup.findAll(text="Location:")
inspector = soup.findAll(text="Inspector:")
body = soup.findAll(text="Comments:")

outfile = open('linnrrs_export.txt', 'w')

for i in range(len( equipid )):
    print "Count=", i
    equipid1 = equipid[i].findNext('td')
    location1 = location[i].findNext('td')
    inspector1 = inspector[i].findNext('td')
    body1 = body[i].findNext('td')
    comments = str(body1.text)
    outfile.write(equipid)
    outfile.write(location1)
    outfile.write(inspector1)
    i = i + 1

outfile.close()