import urllib
from bs4 import BeautifulSoup
import csv

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "linnrrsdbs_subset.xml"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")
tags = soup.findAll('td')
equipid = soup.find(text="Equipment ID:").findNext('td')
location = soup.find(text="Location:").findNext('td')
inspector = soup.find(text="Inspector:").findNext('td')
comments = soup.find(text="Comments:").findNext('td')
#This code prints out the correct format, but does not print unique information for each loop. Just repeats the same information over and over.

#if "Equipment ID:" in 

for tag in tags:
    print equipid.text, location.text, inspector.text
    print comments.text












# for stuff in soup.findAll(text="Equipment ID:"):
#     print "Count=", i
#     equipid = soup.find(text="Equipment ID:").findNext('td') 
#     location = soup.find(text="Location:").findNext('td')
#     inspector = soup.find(text="Inspector:").findNext('td')
#     body = soup.find(text="Comments:").findNext('td')
#     print "Equipment ID:", equipid.text,"Location:", location.text,"Inspector:", inspector.text
#     print "Comments:", body.text

