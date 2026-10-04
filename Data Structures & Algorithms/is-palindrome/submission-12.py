class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        l, r = 0, len(s) - 1

        for i in range(0, len(s)):
            if l < len(s) and r >= 0 and s[l] == s[r] and l <= r:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                return False

        return True