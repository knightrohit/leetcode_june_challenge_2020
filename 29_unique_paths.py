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