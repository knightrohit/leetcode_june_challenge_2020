"""
Time/Space Complexity = O(row*col)
"""

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        if not dungeon:
            return 0
        
        row, col = len(dungeon), len(dungeon[0])
        memo = [[0]*col for _ in range(row)]
        
        for r in reversed(range(row)):
            for c in reversed(range(col)):
                if r == row - 1 and c == col - 1:
                    memo[r][c] = min(0, dungeon[r][c])
                
                elif r == row - 1:
                    memo[r][c] = min(0, dungeon[r][c] + memo[r][c+1])
                    
                elif c == col -1:
                    memo[r][c] = min(0, dungeon[r][c] + memo[r+1][c])

                else:
                    memo[r][c] = min(0, dungeon[r][c] + max(memo[r+1][c], memo[r][c+1]))
           
        return abs(memo[0][0]) + 1