
f = open('p079_keylog.txt', 'r')

data = f.read()

f.close()

data = data.strip().split('\n')

entries = []

for d in data:
    if d not in entries:
        entries.append(d)
entries.sort()

print(entries)
print(len(entries))
