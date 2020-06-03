'''
Time complexity = O(NlogN)
Space complexity = O(N)
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
'''

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        a_set = []
        b_set = []
        costs.sort(key=lambda k: abs(k[0] - k[1]), reverse = True)
        for indx, val in enumerate(costs):
            a, b = val
            if a > b:
                if len(b_set) < len(costs)//2:
                    b_set.append(b)
                else:
                    a_set.append(a)
            else:
                if len(a_set) < len(costs)//2:
                    a_set.append(a) 
                else:
                    b_set.append(b)

        return sum(a_set) + sum(b_set)