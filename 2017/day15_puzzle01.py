a = int(input().split()[4])
b = int(input().split()[4])
total = 0
for i in range(40000000):
	a =  (a * 16807) % 2147483647
	b =  (b * 48271) % 2147483647
	if bin(a)[-16:] == bin(b)[-16:]:
		total += 1
print(total)