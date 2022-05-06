# Files

def getValue(line):
    ipos = line.find('0')
    epos = line.find('\n')
    return float(line[ipos:epos])


filename = "dataset/mbox-short.txt"
fhandle = open(filename, 'r')
count = 0
total = 0
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        count =  count + 1
        total = total + getValue(line)

print("Average spam confidence:", total/count)
        
