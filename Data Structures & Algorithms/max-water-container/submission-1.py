class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        water = 0

        while l < r:
            bounded = min(heights[l], heights[r]) * (r - l)
            print(f"l = {heights[l]}, r = {heights[r]}, r - l = {r - l}, bounded = {bounded}")

            water = max(water, bounded)
            print(f"water = {water}")

            if heights[l] > heights[r]:
                print("r moved inward")
                r -= 1
            
            elif heights[l] < heights[r]:
                print("l moved inward")
                l += 1
            
            elif heights[l] == heights[r]:
                print("both moved inward")
                r -= 1
                l += 1

        return water