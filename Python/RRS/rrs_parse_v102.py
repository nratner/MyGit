import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
from bs4 import BeautifulSoup
import csv

fname = "linnrrsdbs_subset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

i=1
equipid = soup.findAll(text="Equipment ID:")
print len (equipid)
location = soup.findAll(text="Location:")
inspector = soup.findAll(text="Inspector:")
body = soup.findAll(text="Comments:")

myfile = open('linn_rrs_export.txt', 'w')

for i in range(len( equipid )):
    print "Count=", i
    equipid1 = equipid[i].findNext('td')
    location1 = location[i].findNext('td')
    inspector1 = inspector[i].findNext('td')
    body1 = body[i].findNext('td')
    article = (equipid1, location1, inspector1, str(body1.text))
    myfile.write(article)
    i = i + 1

myfile.close()
text_file.close()