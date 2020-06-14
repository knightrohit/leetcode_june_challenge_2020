"""
Time Complexity = O(N^2)
Space Compexity = O(N^2)

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
from collections import defaultdict

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return nums
        
        nums.sort()
        set_dict = defaultdict(set)
        
        for i in nums:
            set_dict[i] = max([set_dict[k] for k in set_dict if i%k == 0], key = len, default = set()) | {i}

        return list(max(set_dict.values(), key = len))