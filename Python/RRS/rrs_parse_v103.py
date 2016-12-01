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

saveFile = open('linn_rrs_export.txt')

for i in range(len( equipid )):
    print "Count=", i
    equipid1 = equipid[i].findNext('td')
    location1 = location[i].findNext('td')
    inspector1 = inspector[i].findNext('td')
    body1 = body[i].findNext('td')
    appendFile.write(equipid1, location1, inspector1,)
    appendFile.write(str(body1.text))
    article = ("Equipment ID:", equipid1.text,"Location:", location1.text,"Inspector:", inspector1.text, "Comments:", str(body1.text))
    i = i + 1

appendFile.close()