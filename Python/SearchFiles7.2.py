#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    #line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
        #print line[pos+1:]
    y = float(line[pos+1:])
    x = 0
    x = x + y
    print x
    #total = 0
    #total = total + y
    #print total
        #total = 0
        #for y in line:
            #total = total + y
        #print total
        #print y, type(y)
        #print line
        #count = 0
        #for x in line:
            #count = count + 1
        #print pos
        
        #print 'Line count:',count
#print 'Done'
    
