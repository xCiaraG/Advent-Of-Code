from sys import stdin
from collections import defaultdict
lines = stdin.readlines()
ranges = defaultdict(int)
for line in lines:
	n1, n2 = [int(x) for x in line.split(": ")]
	ranges[n1] = n2

total = 0
for i in range(max(ranges) + 1):
	if ranges[i] and i % ((ranges[i] - 1) * 2) == 0:
		total += i * ranges[i]

print(total)
