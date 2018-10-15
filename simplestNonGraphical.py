def fillGraph(stones, length):
	graphStones = []
	for i in range(0, length):
		graphStones.append(0)
	graphStones[0] = stones
	return graphStones


def shoot(graphStones, lengthOfGraph):
	tempGraph = []
	for i in range(0, lengthOfGraph):
		tempGraph.append(0)
	for i in range(0, lengthOfGraph):
		if graphStones[i] >= 2:
			tempGraph[i - 1] += 1
			tempGraph[(i + 1)%lengthOfGraph] += 1
			graphStones[i] -= 2
		tempGraph[i] += graphStones[i]
	printGraph(tempGraph)
	return tempGraph


def printGraph(graphStones):
	print(graphStones)


def main():
	graphStones = fillGraph(500, 30)
	length = len(graphStones)
	print(graphStones)

	tempGraph2 = []
	for i in range(0, length):
		tempGraph2.append(0)
	for i in range(0, 2000):
		graphStones = shoot(graphStones, length)
		print(i)
		if tempGraph2 == graphStones:
			print(str(i) + " to reach an equilibrium state")
			break
		tempGraph2 = graphStones.copy()


main()

