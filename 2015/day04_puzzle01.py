from hashlib import md5
s = input().strip()
i = 1
while md5((s + str(i)).encode('utf-8')).hexdigest()[:5] != "00000":
	i += 1
print(i)