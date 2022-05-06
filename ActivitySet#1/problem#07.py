# Strings

text = "X-DSPAM-Confidence:    0.8475 "
ipos = text.find('0')
epos = text.find('\n')
num = float(text[ipos:epos])
print(num)