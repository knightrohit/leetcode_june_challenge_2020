"""
Input : 3
Output : 5

Time Complexity = O(N**2)
Space Complexity = O(N)
"""
class Solution:
    def numTrees(self, n: int) -> int:
        
        if n in [0,1]: return 1
        
        bst = [0]*(n+1)
        bst[0], bst[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                bst[i] += bst[j-1]*bst[i-j]
                
        return bst[n]