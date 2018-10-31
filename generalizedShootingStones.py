"""
Andy J. Wang
runs shooting stones on a variety of graphs
Oct. 31, 2018

"""

class vertex (object):
	name = -1
	stones = 0
	connections = []
	delta = 0

	def __init__(self, n, s, adj):
		self.name = n
		self.stones = s
		self.connections = adj
	def resolveConnections(self):
		for obj in self.connections:
			obj.addConnection(self)

	def addConnection(self, addedVertex):
		if not (addedVertex in self.connections):
			self.connections.append(addedVertex)

	def updateStones(self, n):
		self.stones += n

	"""
	def incrementStones(self):
		self.updateStones(self, 1)
		"""

	def changeDeltas(self, d):
		self.delta += d

	def shoot(self):
		if self.stones >= len(self.connections):
			self.changeDeltas(-1*len(self.connections))
			for obj in self.connections:
				obj.changeDeltas(1)

	def applyDeltas(self):
		self.updateStones(self.delta)
		self.delta = 0

	def display(self):
		a = []
		for obj in self.connections:
			a.append(obj.name)
		return self.name, self.stones, a
	def __str__(self):
		a = ""
		for obj in self.connections:
			a += str(obj.name)
			a += ", "
		return "N: " + str(self.name) + " S: " + str(self.stones) + " adj: " + a

def generateCycle(N, S):
	vertices = []
	vertices.append(vertex(0, 0, []))
	for i in range(1, N):
		vertices.append(vertex(i, 0, [vertices[-1]]))
	vertices.append(vertex(N, 0, [vertices[-1], vertices[0]]))
	vertices[-1].resolveConnections()
	vertices[0].updateStones(S)

	return vertices

def generateConnected(N, S):
	vertices = []
	vertices.append(vertex(0, 0, []))
	for i in range(1, N):
		vertices.append(vertex(i, 0, vertices[::-1]))
		vertices[-1].resolveConnections()
	vertices[0].updateStones(S)

	return vertices

def generatePath(N, S):
	vertices = []
	vertices.append(vertex(0,S,[]))
	for i in range(1,N):
		vertices.append(vertex(i, 0, [vertices[-1]]))
		vertices[-1].resolveConnections()
	return vertices

def doShoots(t, graph):
	for i in range(0, t):
		print("Iteration: " + str(i))
		print("(Vertex number, Stones, Connections)")
		for v in graph:
			v.shoot()
		for v in graph:
			v.applyDeltas()
		for v in graph:
			for l in v.display():
				print(str(l) + "\t", end="")
			#print(v.display())
			print()
		print("\n")

def main():
	graphChoice = int(input("What type of graph?(Cycle (0), Connected (1), Path (2)) "))
	vertexNum = int(input("How many vertices? "))
	stones = int(input("How many stones? "))
	iterations = int(input("How many iterations? "))
	if graphChoice == 0:
		a = generateCycle(vertexNum, stones)
	elif graphChoice == 1:
		a = generateConnected(vertexNum, stones)
	elif graphChoice == 2:
		a = generatePath(vertexNum, stones)
	else:
		print("invalid input")
		return
	for v in a:
		print(v)
	doShoots(iterations, a)


main()
