from sys import stdin
lines = stdin.readlines()
word = ""
for i in range(8):
	d = {}
	for j in range(len(lines)):
		if lines[j][i] in d:
			d[lines[j][i]] += 1
		else:
			d[lines[j][i]] = 1
	word += sorted([(d[k], k) for k in d], reverse=True)[0][1]
print(word)