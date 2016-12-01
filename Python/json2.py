import json

input = '''
[
    {
      "name":"Romina",
      "count":97
    },
    {
      "name":"Laurie",
      "count":97
    },
    {
      "name":"Bayli",
      "count":90
    },
    {
      "name":"Siyona",
      "count":90
    },
    {
      "name":"Taisha",
      "count":88
    },
    {
      "name":"Ameelia",
      "count":87
    },
    {
      "name":"Alanda",
      "count":87
    }
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    #print 'Id', item['id']
    #print 'Attribute', item['x']
    print 'Count', item['count']
