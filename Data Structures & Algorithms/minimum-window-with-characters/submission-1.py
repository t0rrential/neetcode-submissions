class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, matches, shortest = 0, len(t), float('inf')
        sl, sr = 0, 0
        td = {}

        # Build frequency map of t
        for char in t:
            if td.get(char, None) is None:
                td[char] = 0
            td[char] += 1

        for r in range(len(s)):
            if td.get(s[r], None) is not None:
                if td[s[r]] > 0:
                    matches -= 1
                td[s[r]] -= 1

            while matches == 0:
                if r - l + 1 < shortest:
                    sl, sr = l, r + 1
                    shortest = r - l + 1

                if td.get(s[l], None) is not None:
                    td[s[l]] += 1
                    if td[s[l]] > 0:
                        matches += 1

                l += 1

        return s[sl:sr]
