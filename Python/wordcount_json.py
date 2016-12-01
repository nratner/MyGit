import urllib, json

url = 'http://python-data.dr-chuck.net/comments_42.json'
#'http://python-data.dr-chuck.net/comments_217222.json'

#open url
url_open = urllib.urlopen(url)

#extract data
data = url_open.read()

#put the data into a dictionary
data_parsed = json.loads(data)

'''print the sum of all 'count' occurrences. The file has the following structure:
 {
  "note":"This file contains the actual data for your assignment",
  "comments":[
    {
      "name":"abc",
      "count":100
    },
    {
      "name":"cde",
      "count":77
    }, ...
  }
'''
print 'Record count:', len(data_parsed)
print data_parsed

total = 0
for item in data_parsed['comments']:
    total += int(item['count'])

print 'Total: ', total
