
#NOT COMPLETED OR STARTED, REALLY

def fillGraph(toFill):
	graphStones = []
	for i in range(0, len(toFill)):

		graphStones.append(toFill[i])
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
	graphStones = fillGraph([7, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	length = len(graphStones)



	print(graphStones)
	for i in range(0, 200):
		graphStones = shoot(graphStones, length)



main()

