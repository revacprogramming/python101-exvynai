# Tuples

filename = "dataset/mbox-short.txt"

stats = dict()
fhandle = open(filename, 'r')
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    if "From" in words:
        time = words[5]
        hour = time[:2]
        if hour in stats:
            stats[hour] = stats.get(hour, 0) + 1
        else:
            stats.update({hour:1})

counts = list()
for k, v in stats.items():
    counts.append((k, v))

for (k, v) in sorted(counts):
    print(k, v)

