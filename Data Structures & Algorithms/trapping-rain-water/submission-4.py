class Solution:
    def trap(self, height: List[int]) -> int:
        trap = 0

        prefix = []
        prefix.append(height[0])

        suffix = []
        suffix.insert(0, height[len(height) - 1])

        length = len(height)

        for i, e in enumerate(height[1:]):
            i += 1

            prefix.append(max(prefix[i-1], height[i]))


        for i, e in enumerate(height[::-1][1:]):
            suffix.insert(0, max(suffix[0], height[length - 2 - i]))   

        for i in range(length - 1):
            trap += min(prefix[i], suffix[i]) - height[i]

        return trap