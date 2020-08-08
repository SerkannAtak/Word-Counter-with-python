import re
import collections

f = open('mytext.txt', encoding="utf8")
f2 = open('results.txt', 'w',encoding="utf8")
text = f.read()
counts = dict()
splitedArray = re.findall('[\w]+', text)

def count(splitedArray):
    for word in splitedArray:
        if not word.isdigit():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    sortedCounts = collections.OrderedDict(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))

    for k, v in sortedCounts.items():
        f2.write(str(k) + ' >>> ' + str(v) + '\n')
count(splitedArray)
f.close()
f2.close()
