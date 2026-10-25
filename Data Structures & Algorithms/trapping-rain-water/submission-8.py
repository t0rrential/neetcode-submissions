class Solution:
    def trap(self, height: List[int]) -> int:
        m = max(height)
        total = sum((m - x) for x in height)
        t = 0

        # left pass
        for h in height:
            t = max(h, t)

            total -= (m - t)

        # right pass
        t = 0
        for h in reversed(height):
            t = max(h ,t)

            total -= (m - t)

        return total

