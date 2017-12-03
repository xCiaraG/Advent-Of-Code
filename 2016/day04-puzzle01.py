from sys import stdin
from operator import itemgetter

def real(sentence, check):
	d = {}
	for letter in sentence:
		if letter in d:
			d[letter] += 1
		else:
			d[letter] = 1
	s = sorted([(d[l], l) for l in d], key=itemgetter(1))
	s = sorted(s, key=itemgetter(0), reverse=True)
	return s[0][1] + s[1][1] + s[2][1] + s[3][1] + s[4][1] == check


lines = stdin.readlines()
total = 0
for line in lines:
	line = line.strip().split("-")
	if real("".join(line[:-1]), line[-1][4:-1]):
		total += int(line[-1][:3])
print(total)
