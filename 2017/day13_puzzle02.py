from sys import stdin
from collections import defaultdict
lines = stdin.readlines()
ranges = defaultdict(int)
for line in lines:
	n1, n2 = [int(x) for x in line.split(": ")]
	ranges[n1] = n2

total = 1
delay = 0
while total != 0:
	total = 0
	for i in range(max(ranges) + 1):
		if ranges[i] and (i + delay) % ((ranges[i] - 1) * 2) == 0:
			total += 1
			break
	delay += 1

print(delay - 1)