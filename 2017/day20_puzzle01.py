from sys import stdin

class Particle:
	def __init__(self, id, position, velocity, acceleration):
		self.id = id
		self.position = position
		self.velocity = velocity
		self.acceleration = acceleration

	def update(self):
		self.velocity = [self.velocity[i] + self.acceleration[i] for i in range(3)]
		self.position = [self.position[i] + self.velocity[i] for i in range(3)]

	def distance(self):
		return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

def d(item):
	return item.distance()

lines = stdin.readlines()
particles = []
for i in range(len(lines)):
	a, b, c = lines[i].strip().split(", ")
	x1, y1, z1 = a.split(",")
	x2, y2, z2 = b.split(",")
	x3, y3, z3 = c.split(",") 
	position = [int(x1[3:]), int(y1), int(z1[:-1])]
	velocity = [int(x2[3:]), int(y2), int(z2[:-1])]
	acceleration = [int(x3[3:]), int(y3), int(z3[:-1])]
	particles.append(Particle(i, position, velocity, acceleration))

for i in range(10000):
	for p in particles:
		p.update()

print(min(particles, key=d).id)