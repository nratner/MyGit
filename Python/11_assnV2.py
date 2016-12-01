import re
numlist = list()
hand = open('sample11check.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        numlist.append(x)
   
print numlist


# total = 0
# for x in numlist:
#     total = total + x
# print total

