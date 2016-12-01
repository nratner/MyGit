import urllib
from bs4 import BeautifulSoup

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "badhtmlsubset.txt"
hand = open(fname).read()

soup = BeautifulSoup(hand, "html.parser")
equipid= $('#soup td:contains(Equipment ID:)')
i = 1
for stuff in soup
    print i
    print equipid.next().text()

#     print "Equipment ID:", stuff.findNext('td').text,
    #print "Location", stuff.find(text="Location:").findNext('td')   <--Traceback TypeError: find() takes no keyword arguments
        
    i = i + 1

# This code returns the following but I can't get Location, Inspector, or Comments to follow suit.
# Equipment ID: V-2 3
# Equipment ID: Well 79 5
# Equipment ID: AWT-4 6220153-01 (serial number) 7
# Equipment ID: 6220153-02 (serial number) 9
# Equipment ID: Well 3-4 11
# Equipment ID: Well 3-5 13
# Equipment ID: Well 83 15
# Equipment ID: Well 397 17
# Equipment ID: Well 427 19
# Equipment ID: Well 430 21
# Equipment ID: Well 491 23
# Equipment ID: Well 512 Flowline 25
# Equipment ID: Well 513 27
# Equipment ID: Well 555 29
# Equipment ID: Well 583





    
    
