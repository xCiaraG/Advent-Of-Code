keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
from sys import stdin
lines = stdin.readlines()
ans = ""
i, j = 1, 1
for line in lines:
	for d in line:
		if d == "U" and i > 0:
			i -= 1
		elif d == "L" and j > 0:
			j -= 1
		elif d == "R" and j < 2:
			j += 1
		elif d == "D" and i < 2:
			i += 1
	ans += keypad[i][j]
print(ans)

