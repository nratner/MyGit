name = raw_input("Enter file:")
handle = open(name)
#text = handle.read()
#print len(text)
#print text[:100]
#words = text.split()
#print len(words)
#print words

counts = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    if line == [] : continue
    if words[0] != 'From' : continue
    for word in words:
    #if word in counts:
    #if words[0] != 'From' : continue
        counts[word]= counts.get(word,0) + 1 #get method finds word and this sets the first time to "1"
    #print word,"Incremental", counts[word]
    #else:
        #counts[word] = 1
        #print word,"New Word", counts[word]
    print word,counts[word]
    #print words [1]
#print counts.items()
#for kee,val in counts.items() :
    #print kee, val