class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            max_profit = max(max_profit, prices[right]-prices[left])
            if prices[left] > prices[right]:
                left = right
                right = left + 1
            else:
                right = right + 1
        return max_profit

            