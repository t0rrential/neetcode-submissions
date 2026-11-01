class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = -1 
        from math import ceil
        import copy

        def koko(i):
            speed = 0

            for p in piles:
                speed += ceil(p/i)

            return speed

        while l <= r:
            i = (l + r) // 2
            print(i)

            s = koko(i)

            if s <= h:
                ans = i
                r = i - 1
            else:
                l = i + 1

        return ans