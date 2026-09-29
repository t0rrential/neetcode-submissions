class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, len(s) - 1

        lL = 0
        rL = 0

        lU = set()
        rU = set()

        longest = 0

        while l <= len(s) - 1 and r >= 0:
            if s[l] not in lU:
                lU.add(s[l])
                lL += 1
            else:
                lU = set()
                #lU.add(s[l])
                lL = 0
            
            l += 1

            if s[r] not in rU:
                rU.add(s[r])
                rL += 1
            else:
                rU = set()
                #rU.add(s[r])
                rL = 0

            r -= 1

            longest = max(longest, rL, lL)

        return longest

            