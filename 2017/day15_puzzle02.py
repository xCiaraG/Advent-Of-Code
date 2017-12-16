a = int(input().split()[4])
b = int(input().split()[4])
total = 0
for i in range(5000000):
	a =  (a * 16807) % 2147483647
	b =  (b * 48271) % 2147483647
	while a % 4 != 0:
		a *= 16807
		a %= 2147483647
	while b % 8 != 0:
		b *= 48271
		b %= 2147483647
	if bin(a)[-16:] == bin(b)[-16:]:
		total += 1
print(total)