from sys import stdin
lines = stdin.readlines()
total = 0
for line in lines:
	l, w, h = [int(x) for x in line.split("x")]
	total += (2*l) + (2*w) + (2*h) - (2*max(l, w, h)) + (l*w*h)
print(total)