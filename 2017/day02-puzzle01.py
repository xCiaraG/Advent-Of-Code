from sys import stdin
lines = stdin.readlines()
total = 0
for line in lines:
	line = [int(x) for x in line.split()]
	total += max(line) - min(line)
print(total)