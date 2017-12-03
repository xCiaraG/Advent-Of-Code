def add_spiral(l, count):
	#Add right
	for i in range(len(l) - 1, -1, -1):
		l[i].append(count)
		count += 1
	#Add top
	tmp = [count + i for i in range(len(l), -1, -1)]
	count += len(l) + 1
	l = [tmp] + l
	#Add left
	for i in range(len(l)):
		l[i] = [count] + l[i]
		count += 1
	#Add bottom
	l += [[count + i for i in range(len(l) + 1)]]
	count += len(l)
	return l, count

def find_coordinates(l, c):
	for i in range(len(l)):
		for j in range(len(l)):
			if l[i][j] == c:
				return i, j

n = int(input())
current, count = [[1]], 2
while count < n:
	current, count = add_spiral(current, count)

x1, y1 = find_coordinates(current, n)
x2, y2 = find_coordinates(current, 1)
print(abs(x1 - x2) + abs(y1 - y2))
