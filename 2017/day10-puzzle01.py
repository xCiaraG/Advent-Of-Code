numbers = [i for i in range(256)]
lengths = [int(x) for x in input().split(",")]
skip = 0
start = 0
for l in lengths:
	c = 0
	reverse = [numbers[x % len(numbers)] for x in range(start, start + l)]
	reverse.reverse()
	current = start
	for n in reverse:
		numbers[current] = n
		current += 1
		current %= len(numbers)
	start += l + skip	
	start %= len(numbers)
	skip += 1
print(numbers[0]*numbers[1])

