class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        profit = 0

        prefix = []
        prefix.append(prices[0])

        suffix = []
        suffix.append(prices[len(prices) - 1])

        for i, e in enumerate(prices[1:]):
            prefix.append(min(prefix[i], prices[i + 1]))
            
        for i, e in enumerate(prices[::-1][1:]):
            suffix.insert(0, max(suffix[0], prices[length - i - 2]))

        print(prefix)
        print(suffix)

        for i in range(length):
            profit = max(profit, suffix[i] - prefix[i])

        return profit
