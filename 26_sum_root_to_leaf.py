"""
Input: [1,2,3]
Output: 25
Time/Space Complexity = O(N)
"""

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        out = 0
        def dfs(node, val=0):
            nonlocal out
            if node:
                val = val*10 + node.val

                if not (node.left or node.right):
                    out += val
                    return

                dfs(node.left, val)
                dfs(node.right, val)
           
        dfs(root)
        return out