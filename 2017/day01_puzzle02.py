numbers = input().strip()
total = 0
for i in range(len(numbers)):
	if numbers[i] == numbers[(i+len(numbers)//2) % len(numbers)]:
		total += int(numbers[i])
print(total)