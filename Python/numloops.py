largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : 
    #if len(num) < 1 :
        print "Invalid input"
        break
    num = float(num)
    try:
        if smallest is None or num < smallest:
            smallest = num
            print "Loop: ", num, smallest
    except:
        print "This program only accepts numeric values"
        quit()
    try:
        if largest is None or num > largest:
            largest = bignum
            print "Loop: ", num, smallest, bignum, largest
    except:
        print "This program only accepts numeric values"
        quit()
    
    print num

print "Maximum is", largest
print "Minimum is", smallest