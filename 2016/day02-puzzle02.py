keypad = [[0, 0, "1", 0, 0],          \
          [0, "2", "3", "4", 0],      \
          ["5", "6", "7", "8", "9"],  \
          [0, "A", "B", "C", 0],      \
          [0, 0, "D", 0, 0]]
from sys import stdin
lines = stdin.readlines()
ans = ""
i, j = 2, 0
for line in lines:
	for d in line:
		if d == "U" and i > 0 and keypad[i-1][j]:
			i -= 1
		elif d == "L" and j > 0 and keypad[i][j-1]:
			j -= 1
		elif d == "R" and j < 4 and keypad[i][j+1]:
			j += 1
		elif d == "D" and i < 4 and keypad[i+1][j]:
			i += 1
	ans += keypad[i][j]
print(ans)