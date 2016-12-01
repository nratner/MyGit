#import urllib
import xml.etree.ElementTree as ET

# url = raw_input('Enter - ')
# serviceurl = urllib.urlopen(url).read()
data = '''
<commentinfo>
<note>This file contains the sample data for testing</note>
<comments>
<comment>
<name>Romina</name>
<count>97</count>
</comment>
<comment>
<name>Laurie</name>
<count>97</count>
</comment>'''

tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Count:',tree.find('count').text

# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break
# 
#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#     print data
#     tree = ET.fromstring(data)
# 
#     counts = tree.findall('.//count')
# 
#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text
# 
#     print 'lat',lat,'lng',lng
#     print location