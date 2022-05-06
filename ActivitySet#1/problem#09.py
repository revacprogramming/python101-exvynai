# Lists

filename = "dataset/romeo.txt"
fhandle = open(filename,'r')
all_words = []
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if all_words.count(word) == 0:
            all_words.append(word)

all_words.sort()
print(all_words)