# Upper Bound: O(n!) time | O(n) space - where n is the input number
class Solution:
  	def nonAttackingQueens(n):
    	blockedColumns = set() 
    	blockedUpDiagonals = set() 
    	blockedDownDiagonals = set() 
    	return getNumberOfNonAttackingQueenPlacements(0, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, n)
  
  	def getNumberOfNonAttackingQueenPlacements(row, blockedColumns, blockedupDiagonals, blockedDownDiagonals, boardSize):
    	if row == boardSize:
      		return 1
    
    validplacements = 0 
    for col in range (boardsize): 
      if isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals:
    	  placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals) 
          validplacements += getNumberOfNonAttackingQueenPlacements(
          	row + 1, blockedColumns, blockedUpDiagonals, blockedDownDiagonals, boardSize
          )
          removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals)
                                  
    return validPlacements
                                  
# This is always an 0(1) time operation. 
	def isNonAttackingPlacement(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals): 
		if col in blockedColumns:
			return False 
        if row + col in blockedUpDiagonals:
			return False 
        if row - col in blockedDownDiagonals:
			return False
		
        return True
                                  
	def placeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
		blockedColumns.add(col) 
    	blockedUpDiagonals.add(row + col) 
    	blockedDownDiagonals.add(row - col)
    
    def removeQueen(row, col, blockedColumns, blockedUpDiagonals, blockedDownDiagonals):
		blockedColumns.remove(col) 
    	blockedUpDiagonals.remove(row + col) 
    	blockedDownDiagonals.remove(row - col)
