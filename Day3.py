def numberOfBinaryTreeTopologies(n):
    
    return calculateNumberOfTopologies(n, {0: 1})

def calculateNumberOfTopologies(n, cache):
	if n in cache:
		return cache[n]
	
	total = 0
	for i in range(0, n):
		topologiesInLeftSubtree = calculateNumberOfTopologies(i, cache)
		topologiesInRightSubtree = calculateNumberOfTopologies(n - i - 1, cache)
		total += topologiesInLeftSubtree * topologiesInRightSubtree
	
	cache[n] = total
	return total
