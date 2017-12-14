numbers = input().strip()
total = 0
for i in range(len(numbers)):
	if numbers[i] == numbers[(i+1) % len(numbers)]:
		total += int(numbers[i])
print(total)