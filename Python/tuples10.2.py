#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

 
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    #line = line.rstrip()
    words = line.split()
    if words == [] : continue
    if words[0] != 'From' : continue
    msghour = words[5]
    msghour = msghour[:2]
    counts[msghour] = counts.get(msghour,0) + 1
#hours = sorted( counts.items() )    
#print hours debugging and this worked. just need print out

for k,v in sorted( counts.items() ):
    print k, v
    
    
# lst = list()
# for key,val in counts.items():
#     lst.append( (key, val) )
# lst.sort(reverse=True)
# for key,val in lst[]:
#     print key, val
#this is for reversing k & v and not needed.


#print counts.items()