import numpy as np
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
	#printGraph(tempGraph)
	return tempGraph


def printGraph(graphStones):
	print(graphStones)


def playGame(n1, n2, doPrint=False):
	graphStones = fillGraph(n1, n2)
	length = len(graphStones)
	print(graphStones)

	tempGraph2 = []
	tempGraph3 = []
	for i in range(0, length):
		tempGraph2.append(0)
		tempGraph3.append(0)
	i = 0
	while(True):
		i += 1
		graphStones = shoot(graphStones, length)
		yield graphStones
		if doPrint:
			#print(i)
			print(graphStones)
		if tempGraph2 == graphStones:
			if doPrint:
				print(str(i) + " to reach an imobile equilibrium state")
			#return 1
			break
		if tempGraph3 == graphStones:
			if doPrint:
				print(str(i) + " to reach an 2-oscilating equil state")
			#return 2
			break
		tempGraph3 = tempGraph2.copy()
		tempGraph2 = graphStones.copy()
	#return 3

def main():
	"""
	for l in playGame(20,10,False):
		print(l)
		"""

	fullList = []
	for i, lst in enumerate(playGame(22,11,False)):
		print(lst)
		listv = lst.copy()
		fullList.append(listv)
		#fullList.insert(i, listv)
	print(fullList)
	rotatedEverything = []
	for x in range(0, len(fullList[0])):
		rotatedEverything.append([])
		for y in range(0, len(fullList)):
			rotatedEverything[x].append(-1)

	for x in range(0, len(fullList)):
		for y in range(0, len(fullList[x])):
			rotatedEverything[y][x] = fullList[x][y]

	for line in rotatedEverything:
		print("\n")
		for num in line:
			print(str(num) + "\t", end="")


	"""
	for i in range(1, 100):
		for q in range(1, 100):
			print(str(i) +", " + str(q) +": ")
			if(playGame(i, q) == 3):
				print("this ain't it chief")
				return
				"""

main()

