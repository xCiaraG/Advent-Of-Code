from collections import defaultdict

def remove_difference(d, d1, d2):
	tmp = min(d[d1], d[d2])
	d[d1] -= tmp
	d[d2] -= tmp
	return d

def substitute(d, d1, d2, d3):
	tmp = min(d[d1], d[d2])
	d[d1] -= tmp
	d[d2] -= tmp
	d[d3] += tmp
	return d


directions = input().split(",")
d = defaultdict(int)
for direction in directions:
	d[direction] += 1

tmp = {}
while tmp != d:
	tmp = d
	d = remove_difference(d, "n", "s")
	d = remove_difference(d, "ne", "sw")
	d = remove_difference(d, "nw", "se")
	d = substitute(d, "ne", "s", "se")
	d = substitute(d, "se", "sw", "s")
	d = substitute(d, "s", "nw", "sw")
	d = substitute(d, "sw", "n", "nw")
	d = substitute(d, "nw", "ne", "n")
	d = substitute(d, "n", "se", "ne")
print(sum(d.values()))

