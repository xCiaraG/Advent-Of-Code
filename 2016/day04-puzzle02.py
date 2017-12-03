from sys import stdin

alphabet = "abcdefghijklmnopqrstuvwxyz"

def decrypt(sentence, sec_id):
	s = ""
	for letter in sentence:
		if letter in alphabet:
			s += alphabet[(alphabet.index(letter) + sec_id) % 26]
		else:
			s += letter
	if "north" in s:
		print(s, sec_id)
	return


lines = stdin.readlines()
total = 0
for line in lines:
	line = line.strip().split("-")
	decrypt(" ".join(line[:-1]), int(line[-1][:3]))