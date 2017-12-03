from sys import stdin
lines = stdin.readlines()
t = 0
for line in lines:
	x, y, z = [int(x) for x in line.split()]
	if x + y > z and x + z > y and y + z > x:
		t += 1
print(t)