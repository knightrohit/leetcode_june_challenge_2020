"""
Time/Space Complexity = O(N)
"""
# Top Down Apporach
from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache
        def dfs(row = 0, col = 0):

            if row == m - 1 and col == n - 1:
                return 1 
            
            if row >= m or col >= n:
                return 0

            return dfs(row, col+1) + dfs(row+1, col)

        return dfs()



#DP - Botton up approach
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = [[0]*n for _ in range(m)]
        
        for i in range(m):
            memo[i][n-1] = 1
        
        for j in range(n):
            memo[m-1][j] = 1
            
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):                
                memo[row][col] = memo[row][col+1] + memo[row+1][col]
                
        return memo[0][0]