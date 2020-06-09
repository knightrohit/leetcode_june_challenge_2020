"""
Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false

Time Complexity = O(N)
Space Complexity = O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s and not t:
            return True
        
        if not t:
            return False
        
        if not s:
            return True
        
        j = 0
        for i in t:
            if s[j] == i:
                if j == len(s) - 1:
                    return True
                j += 1
                continue
            
        return False