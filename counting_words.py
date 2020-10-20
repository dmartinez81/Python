
from string import punctuation
# read from file, remove caps and punctuation, and split into words
# text = open( ' romeoandjuliet.txt ' ).read()
# text = open( '/home/diego/Programming/Nick-White-problems-2/Programming/C++/Analyzer.py' ).read()
text = open( '/home/diego/Git/youtube-dl/README.txt' ).read()

text = text.lower()
for p in punctuation:
    text = text.replace(p, '' )
words = text.split()
# build the dictionary of frequencies
d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1

# print in alphabetical order

items = list(d.items())
items.sort()

for i in items:
    print(i)

# print in order from least to most common

items = list(d.items())
items = [(i[1], i[0]) for i in items]
items.sort()

for i in items:
    print(i)
