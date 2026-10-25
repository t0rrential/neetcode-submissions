class Solution:
    def trap(self, height: List[int]) -> int:
        m, l= max(height), len(height)
        total = sum((m - x) for x in height)
        t = float('-inf')

        print(total)

        # left pass
        for h in height:
            t = max(h, t)

            total -= (m - t)

        # right pass
        t = float('-inf')
        for h in reversed(height):
            t = max(h ,t)

            total -= (m - t)

        return total

