class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)          # update lowest price so far
            max_profit = max(max_profit, price - min_price)  # update profit if better

        return max_profit