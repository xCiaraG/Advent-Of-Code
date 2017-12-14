from day10_puzzle02 import knot_hash
word = input().strip()
total = 0
for i in range(128):
	knot = knot_hash(word + "-" + str(i))
	s = ""
	for d in knot:
		s += bin(int(d, base=16))[2:]
	total += s.count("1")
print(total)
