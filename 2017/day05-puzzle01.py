from sys import stdin
lines = stdin.readlines()
total = 0
numbers = [int(x) for x in lines]
i, c = 0, 0
while i < len(numbers):
	numbers[i] += 1
	i += numbers[i] - 1
	c += 1
print(c)