class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, freq, w = 0, 0, 0
        most = defaultdict(int)

        for r in range(len(s)):
            most[s[r]] += 1

            freq = max(most[s[r]], freq)

            # contract window
            while (r - l + 1) - freq > k:
                most[s[l]] -= 1
                l += 1 

            w = max(w, r-l+1)

        return w