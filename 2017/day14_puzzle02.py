from day10_puzzle02 import knot_hash

def dfs(i, j):
	visited = set([])
	to_check = [(i, j)]
	while to_check:
		i, j = to_check.pop(0)
		if i >= 0 and i < len(maze) and j >= 0 and j < len(maze[0]) and maze[i][j] == "1" and (i, j) not in visited:
			maze[i][j] = "0"
			visited.add((i, j))
			to_check.append((i + 1, j))
			to_check.append((i - 1, j))
			to_check.append((i, j + 1))
			to_check.append((i, j - 1))

word = input().strip()
maze = []
for i in range(128):
	knot = knot_hash(word + "-" + str(i))
	s = ""
	for d in knot:
		tmp = bin(int(d, base=16))[2:]
		tmp = "0"*(4 - len(tmp)) + tmp
		s += tmp
	maze.append(list(s))
count = 0
for i in range(len(maze)):
	for j in range(len(maze[0])):
		if maze[i][j] == "1":
			count += 1
			dfs(i, j)
print(count)