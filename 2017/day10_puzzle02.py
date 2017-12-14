def knot_hash(sequence):
	numbers = [i for i in range(256)]
	lengths = [ord(c) for c in sequence] + [17, 31, 73, 47, 23]
	skip = 0
	start = 0
	for _ in range(64):
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

	dense_hash = []
	for i in range(0, len(numbers), 16):
		current = 0
		for j in range(i, i + 16):
			current ^= numbers[j]
		dense_hash.append(current)
	knot_hash = "".join([hex(n)[2:] if n > 15 else "0" + hex(n)[2:] for n in dense_hash])
	return knot_hash

def main():
	sequence = input().strip()
	print(knot_hash(sequence))

if __name__ == "__main__":
	main()