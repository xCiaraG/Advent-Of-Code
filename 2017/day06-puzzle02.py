from sys import stdin
numbers = [int(x) for x in input().split()]
total = 0
seen = []
while " ".join([str(x) for x in numbers]) not in seen:
	seen.append(" ".join([str(x) for x in numbers]))
	tmp = max(numbers)
	j = numbers.index(tmp)
	tmp2 = tmp // (len(numbers) - 1)
	for i in range(len(numbers)):
		if i != j:
			numbers[i] += tmp2
		else:
			numbers[j] = tmp % (len(numbers) - 1)
	if tmp2 == 0:
		numbers[j] = 0
		i = j + 1
		while tmp != 0:
			numbers[i % len(numbers)] += 1
			i += 1
			tmp -= 1
	total += 1
print(total - seen.index(" ".join([str(x) for x in numbers])))