import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
from bs4 import BeautifulSoup
import csv

fname = "linnrrsdbs_subset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

articles = soup.findAll('tbody')
i=0
equiptag = soup.findAll(text="Equipment ID:")
locationtag = soup.findAll(text="Location:")
inspectortag = soup.findAll(text="Inspector:")
bodytag = soup.findAll(text="Comments:")

for tag in articles:
    equipid = equiptag.findNext('td')
    if equipid not in articles:
        articles.append(equipid)

    # equiptag = soup.findAll(text="Equipment ID:")
    #for child in equiptag:
        # equipid = childtag.string
        # print child[5]





#     if equipid not in articles:
#         articles.append(equipid)
#
# for i in articles:
#     print i


#print len(articles)