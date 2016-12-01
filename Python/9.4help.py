# "9.4" => Array(
# "qtext" => "<b>9.4</b> Write a program to read through the <b>mbox-short.txt</b> and figure
# out who has the most commits.  The program looks for 'From ' lines and takes the second
# word of those lines as the person who sent the mail.  The program creates a Python 
# dictionary that maps the senders mail address to a count of the number of times

# they appear in the file.  After the dictionary is produced, the program reads through
# the dictionary using a maximum loop to find the most prolific committer.",
# "desired" => "cwen@iupui.edu 5",
name = raw_input("Enter file:")
if len(name) < 1 : name = "usepython_to get u_fieldname.txt"
handle = open(name)

for line in handle:
    if not line.startswith("From:") : continue
    words = line.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1 

        
maxval = None
mostsent = None
for key,val in counts.items() :
    if maxval == None or maxval > val :
        maxval = val
        mostsent = key   

print mostsent, maxval