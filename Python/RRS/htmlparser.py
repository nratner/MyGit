from mechanize import Browser
fname = raw_input("Enter file name: ")
fhtml = open(fname)
content = fhtml.read
br = Browser()
br.open('http://somewebpage')
html = br.response().readlines()
for line in html:
  print line