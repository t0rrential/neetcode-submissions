class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        l, r = 0, 0

        while r != len(s):
            c = s[r]

            if c in seen:
                longest = max(longest, r - l)

                while s[l] != c:
                    seen.discard(s[l])
                    l += 1
                l += 1

            else:
                seen.add(c)
            
            r += 1


        return max(longest, r - l)

                
