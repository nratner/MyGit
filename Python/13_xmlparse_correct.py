import urllib
import xml.etree.ElementTree as ET


#ask what file to open
url = raw_input('Enter URL:')
#Test Source: http://python-data.dr-chuck.net/comments_42.xml
#Actual Source: http://python-data.dr-chuck.net/comments_293417.xml

#open and read the file
serviceurl = urllib.urlopen(url).read()

# transform the string into an object
tree = ET.fromstring(serviceurl)

# find all of the count elements
counts = tree.findAll('.//count')
# regex for counts = tree.findall('comments/comment/count')

# sum up all of the count elements and provide a total
total = 0
for count in counts:
    total += int(count.text)
print 'Count:', len(counts)
print 'Sum: ', total
