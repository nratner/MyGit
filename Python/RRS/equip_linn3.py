import xml.etree.ElementTree as ET

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "linnrrsdbs_subset.xml"
stuff = ET.parse(fname)

all = stuff.findall('html/table/tbody')
print 'Article count:', len(all)


