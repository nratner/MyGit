#normal way

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print atpos

sppos = data.find(' ',atpos)
print sppos

host = data[atpos+1 : sppos]
print host

#double split
words = line.split()
email = words[1]
pieces = email.split('@')
print pieces[1]

#regex
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print y
