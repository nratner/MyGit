import urllib
from bs4 import BeautifulSoup
#import xml.etree.ElementTree as ET

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "LINN_rrs_subset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")

for stuff in soup:
    equipid = soup.find(text="Equipment ID:").findNext('td')
    location = soup.find(text="Location:").findNext('td')
    inspector = soup.find(text="Inspector:").findNext('td')
    body = soup.find(text="Comments:").findNext('td')
    print equipid.text
    print location.text
    print inspector.text
    print body.text






#count = 0
# tags = soup.findAll('td')
# print(soup.td[0].text)
# for tag in tags:
#     count = count + 1
# 
# print 'Number of p tags:', count
#print (soup.p(6))

# for tag in tags:
#     if tag == [] : continue
#print tags









# 
# # find all of the count elements
# counts = tree.findall('.//span')
# # regex for counts = tree.findall('comments/comment/count')
# 
# # sum up all of the count elements and provide a total
# total = 0
# for count in counts:
#     total += int(count.text)
# print 'Count:', len(counts)
#print 'Sum: ', total