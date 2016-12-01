import re
#total = 0
x = 'Why should you learn to write programs? 7746 12 1929 8827 Writing programs (or programming) is a very creative 7 and rewarding activity.  You can write programs for many reasons, ranging from making your living to solving 8837 a difficult data analysis problem to having fun to helping 128 someone else solve a problem.  This book assumes that everyone needs to know how to program ...'
#hand = open('sample11check.txt')
#lines = hand.read(x)
nums = re.findall('[0-9]+',lines)
nums= int(nums)
print nums
#prep = float(nums)
#total = 0
# for x in nums:
#     if len(x) > 0 :
#     total = total + x
#     print total