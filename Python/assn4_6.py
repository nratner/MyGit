def computepay(h,r) :
    if h <= 40 :
    	p = r * h
        return p
	else :
	    p = r * 40 + (r * 1.5 * (h - 40))
    	return p

try:
    hours = raw_input("Enter Hours:")
    hours = float(hours)
    rate = raw_input("Enter Hourly Rate:")
    rate = float(rate)
except:
    print "This program only accepts numeric values"
    quit()

grosspay = computepay(hours, rate)
print grosspay

#hrs = raw_input("Enter Hours:")
#p = computepay(10,20)
#print "Pay",p
