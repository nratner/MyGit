text = "X-DSPAM-Confidence:    0.8475";
print text
pos = text.find(':')
print pos
print text[pos+1:]
y = float(text[pos+1:])
print y, type(y)

