import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
from bs4 import BeautifulSoup
import csv

fname = "usepython_to get u_fieldname.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

#This code prints out the correct format, but does not print unique information for each loop. Just repeats the same information over and over.
i=1


for i in range(len( equipid )):
    print "Count=", i
    equipid1 = equipid[i].findNext('td')
    location1 = location[i].findNext('td')
    inspector1 = inspector[i].findNext('td')
    body1 = body[i].findNext('td')
    print "Equipment ID:", equipid1.text,"Location:", location1.text,"Inspector:", inspector1.text
    print "Comments:", str(body1.text)
    i = i + 1