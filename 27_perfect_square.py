"""
Input: 12
Output: 3
Time Complexity = O(n*(n**0.5)) = O(n**1.5)
Space Compexity = O(n)
"""

class Solution:
    def numSquares(self, n: int) -> int:        
        # dp formula, it's bottom up approach
        # min_val = min(min_val, dp[i-j])
        # dp[i] = min_val + 1
        
        if n == 1 or n == int(n**0.5)**2:
            return 1
        
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            j, sq = 1, 1
            min_val = i
            while sq <= i:
                min_val = min(min_val, dp[i-sq])
                j += 1
                sq = j**2

            dp[i] = min_val+1
            
        return dp[n]