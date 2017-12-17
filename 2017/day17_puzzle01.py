current = 1
n = 356	
l = [0]
for i in range(1, 2018):
	l.insert(current, i)
	current = (current + n + 1) % len(l)
tmp = l.index(2017)
print(l[(tmp + 1) % len(l)])