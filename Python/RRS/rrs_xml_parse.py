import urllib
import xml.etree.ElementTree as ET

#ask what file to open
#url = raw_input('Enter URL:')
#Test Source: http://python-data.dr-chuck.net/comments_42.xml
#Actual Source: http://python-data.dr-chuck.net/comments_293417.xml

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "linnrrsdbs.xml"
hand = open(fname).read()


#open and read the file
serviceurl = urllib.urlopen(hand).read()

# transform the string into an object
tree = ET.fromstring(serviceurl)

# find all of the count elements
counts = tree.findall('html')
# regex for counts = tree.findall('comments/comment/count')

# sum up all of the count elements and provide a total
total = 0
for count in counts:
    total += int(count.text)
#print 'Count:', len(counts)
print 'Number of Articles: ', total
