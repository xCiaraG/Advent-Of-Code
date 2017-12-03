from sys import stdin
lines = stdin.readlines()
total = 0
for line in lines:
	line = [int(x) for x in line.split()]
	for i in line:
		for j in line:
			if i != j and i % j == 0:
				total += i // j 
print(total) 