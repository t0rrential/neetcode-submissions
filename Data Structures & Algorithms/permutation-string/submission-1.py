class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0

        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(s1)):
            c1[ord(s1[i]) - 97] += 1

        for r in range(len(s2)):
            c2[ord(s2[r]) - 97] += 1

            #print(f"on window {s2[l:r]}")

            if (r - l + 1) >= len(s1) + 1:
                c2[ord(s2[l]) - 97] -= 1
                l += 1

            #print(f"adjusted to window {s2[l:r]}")

            if c1 == c2:
                return True

        return False