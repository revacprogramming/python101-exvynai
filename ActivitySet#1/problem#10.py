# Dictionaries

filename = "dataset/mbox-short.txt"

fhandle = open(filename, 'r')
stats = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if "From" in words:
        name = words[1]
        if name in stats:
            stats[name] = stats.get(name, 0) + 1
        else:
            stats.update({name:1})

temp = stats.values()
max_value = max(temp)

for k, v in stats.items():
    if v == max_value:
        print(k, v)




