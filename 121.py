class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_prof = 0
        for price in prices:
            prof = price - lowest_price
            max_prof = max(prof, max_prof)
            lowest_price = min(lowest_price, price)

        return max_prof
