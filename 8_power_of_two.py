"""
Time/Space complexity = O(1)
Input: 16
Output: true

Input: 218
Output: false
"""

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        val = math.log2(n)
        return val - int(val) == 0