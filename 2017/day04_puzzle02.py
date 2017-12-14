from sys import stdin
lines = stdin.readlines()
total = 0
for line in lines:
	tmp = line.strip().split()
	words = []
	for word in tmp:
		words.append("".join(sorted(word)))
	if len(words) == len(set(words)):
		total += 1
print(total)