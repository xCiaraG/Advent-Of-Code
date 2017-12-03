from sys import stdin
lines = stdin.readlines()
t = 0
triangles = []
for line in lines:
	triangles.append([int(x) for x in line.split()])

for i in range(0, len(triangles), 3):
	for j in range(3):
		x, y, z = triangles[i][j], triangles[i+1][j], triangles[i+2][j]
		if x + y > z and x + z > y and y + z > x:
			t += 1
print(t)