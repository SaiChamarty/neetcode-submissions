class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, num_i in enumerate(prices):
            for j, num_j in enumerate(prices):
                if i < j:
                    max_profit = max((num_j - num_i), max_profit)
        return max_profit