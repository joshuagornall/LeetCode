# O(N^2) time and O(N) space
def minimumAreaRectangle(points):
	pointSet = createPointSet(points)
	minimumAreaFound = float("inf")
	
	for currentIdx, p2 in enumerate(points):
		p2x, p2y = p2
		for previousIdx in range(currentIdx):
			p1x, p1y = points[previousIdx]
			pointsShareValue = p1x == p2x or p1y == p2y
			
			if pointsShareValue:
				continue
				
			point1OnOppositeDiagonalExists = convertPointToString(p1x, p2y) in pointSet
			point2OnOppositeDiagonalExists = convertPointToString(p2x, p1y) in pointSet
			oppositeDiagonalExists = point1OnOppositeDiagonalExists and point2OnOppositeDiagonalExists
			
			if oppositeDiagonalExists:
				currentArea = abs(p2x - p1x) * abs(p2y - p1y)
				minimumAreaFound = min(minimumAreaFound, currentArea)
				
	return minimumAreaFound if minimumAreaFound != float("inf") else 0

def createPointSet(points):
	pointSet = set()
	
	for point in points:
		x, y = point
		pointString = convertPointToString(x, y)
		pointSet.add(pointString)
		
	return pointSet

def convertPointToString(x, y):
	return str(x) + ":" + str(y)
