import re
total=0
hand = open('11_actual.txt')
for line in hand:
    line = line.rstrip()
    listnumbers = re.findall('[0-9]+', line)
    if len(listnumbers) > 0:
        for num in listnumbers:
            num = int(num)
            total = total + num
            
  
print total

# total = 0
# for x in numlist:
#     total = total + x
# print total

