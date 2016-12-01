from HTMLParser import HTMLParser

class HTMLCleaner(HTMLParser):

    container = ""
    
    def handle_data(self, data):
        self.container += data
        return self.container
        
h = HTMLCleaner()
fname = raw_input("Enter file name: ")
fhtml = open(fname)
content = fhtml.read