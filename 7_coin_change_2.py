"""
Time/Space Complexity = O(N)
Input: amount = 5, coins = [1, 2, 5]
Output: 4
"""
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def count_coins(amt, indx):
            if amt == 0:return 1
            
            if amt < 0 or indx == len(coins):
                return 0
            
            curr_res = 0
            
            for i, coin in enumerate(coins[indx:], indx):
                curr_res += count_coins(amt - coin, i)
            return curr_res
    
        coins.sort(reverse=True)
        return count_coins(amount, 0)