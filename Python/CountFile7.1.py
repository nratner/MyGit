fname = raw_input("Enter file name: ")
count=0
total=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    num = float(line[pos+1:])
    count = count + 1
    total = total + num

print 'Average spam confidence:', total/count

    
   
