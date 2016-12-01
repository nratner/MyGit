import urllib
import json


#ask what file to open
url = raw_input('Enter URL:')
#test url: http://python-data.dr-chuck.net/comments_42.json
#assignment url: http://python-data.dr-chuck.net/comments_293421.json

#open and read the file
html = urllib.urlopen(url).read()

# deserialize step
info = json.loads(html)

total = 0
for counts in info['comments']:
        total += int(counts['count'])

print 'Sum: ', total










