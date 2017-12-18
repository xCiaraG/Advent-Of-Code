from collections import defaultdict
houses = defaultdict(int)
directions = input().strip()
x, y = 0, 0
houses[(0, 0)] = 1
nsew = {"<" : (-1, 0), ">" : (1, 0), "^" : (0, 1), "v" : (0, -1)}
for d in directions:
	x += nsew[d][0] 
	y += nsew[d][1]
	houses[(x, y)] += 1
print(len(houses))