"""
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

Time/Space Complexity = O(V**2)
"""
from queue import PriorityQueue
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        if not flights:
            return -1
        
        adj = defaultdict(list)
        
        for s, d, c in flights:
            adj[s].append((d, c))
            
        q = PriorityQueue()
        q.put((0, src, K+1))
        
        while not q.empty():
            c, n, k = q.get()
            if n == dst:
                return c
            if k > 0:
                for n_n, n_c in adj[n]:
                    q.put((c+n_c, n_n, k-1))
                    
        return -1    
        