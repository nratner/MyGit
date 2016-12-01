from bs4 import BeautifulSoup
import re


name = raw_input("Enter file:")
if len(name) < 1 : name = "usepython_to get u_fieldname.txt"
handle = open(name)

soup = BeautifulSoup(handle, "html.parser")

snfields = []
# for loop looks for all td tags
for link in soup.findAll('td'):
    #create a value to strip the tags
    field = link.text
    #create a value to split on the '_' symbol
    fieldname = str(field).split('_')
    #create a value to split the drop the '}' from the end
    fieldtext =str(fieldname[1]).split('}')
    #create a value that drops the ';' from the end
    fieldvalue = str(fieldtext[0]).split(';')
    #append only unique values to the list
    if fieldvalue[0] not in snfields:
        snfields.append(fieldvalue[0])

for i in snfields:
    print i




