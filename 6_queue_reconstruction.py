"""
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Time complexity = O(N^2)
Space complexity = O(N)
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key = lambda x : (-x[0], x[1]))
        out = []
        for i in people:
            out.insert(i[1], i)
            
        return out