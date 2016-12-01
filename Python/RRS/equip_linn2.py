import urllib
from bs4 import BeautifulSoup


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'linnrrsdbs_subset.txt'

hand = open(fname).read()


soup = BeautifulSoup(hand, "html.parser")


