current = 1
n = 356
ans = 0
for i in range(1, 50000001):
	if current == 1:
		ans = i
	current = ((current + n) % (i + 1)) + 1
print(ans)