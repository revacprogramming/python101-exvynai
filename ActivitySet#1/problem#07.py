# Strings

text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find('0')
num = float(text[ipos:ipos+7])
print(num)