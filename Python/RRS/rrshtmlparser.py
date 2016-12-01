# from lxml import etree
# 
# tree = etree.parse('Linn_site_sample.txt')
# notags = etree.tostring(tree, encoding='utf8', method='text')
# print(notags)

import re

url = raw_input("Enter file name: ")
html = open(url).read()
#content = fhtml.read

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(html):
    return TAG_RE.sub('', html)
    
print html    
