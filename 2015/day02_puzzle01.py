from sys import stdin
lines = stdin.readlines()
total = 0
for line in lines:
	l, w, h = [int(x) for x in line.split("x")]
	total += (2*l*w) + (2*w*h) + (2*l*h) + min((l*w), (w*h), (l*h))
print(total)