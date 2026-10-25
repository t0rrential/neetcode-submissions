class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lp = 101

        for p in prices:
            lp = min(p, lp)

            profit = max(profit, p - lp)

        return profit



