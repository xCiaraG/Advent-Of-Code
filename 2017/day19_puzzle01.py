from sys import stdin

def in_bounds(x, y):
   return 0 <= x < len(m) and 0 <= y < len(m[0])

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lines = stdin.readlines()
m = []
for line in lines:
   m.append(list(line)[:-1])

x, y = 0, m[0].index("|")
tmpx, tmpy = x, y
ans = ""
seen = set([(x, y)])
nsew = {"n" : (-1, 0), "s" : (1, 0), "e" : (0, 1), "w" : (0, -1)}
d = "s"
while True:
   while in_bounds(tmpx, tmpy) and m[tmpx][tmpy].strip():
      if m[tmpx][tmpy] in ALPHABET:
         ans += m[tmpx][tmpy]
      x = tmpx
      y = tmpy
      seen.add((x, y))
      tmpx += nsew[d][0]
      tmpy += nsew[d][1]
   if in_bounds(x - 1, y) and (x - 1, y) not in seen and m[x - 1][y].strip():
      tmpx = x - 1
      tmpy = y
      d = "n"
   elif in_bounds(x + 1, y) and (x + 1, y) not in seen and m[x + 1][y].strip():
      tmpx = x + 1
      tmpy = y
      d = "s"
   elif in_bounds(x, y - 1) and (x, y - 1) not in seen and m[x][y - 1].strip():
      tmpx = x 
      tmpy = y - 1
      d = "w"
   elif in_bounds(x, y + 1) and (x, y + 1) not in seen and m[x][y + 1].strip():
      tmpx = x
      tmpy = y + 1
      d = "e"
   else: 
      break
print(ans)