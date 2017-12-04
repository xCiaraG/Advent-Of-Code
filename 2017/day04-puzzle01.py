from sys import stdin
lines = stdin.readlines()
total = 0
for line in lines:
	words = line.strip().split()
	if len(words) == len(set(words)):
		total += 1
print(total)