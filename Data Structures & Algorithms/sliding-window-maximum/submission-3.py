class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxArr = []
        m = float("-inf")
        maxIdx = -1

        l = 0

        for r in range(len(nums)):
            if (r - l + 1) > k:
                l += 1
            print(f"on {nums[r]}, nums[{l}:{r}] = {nums[l:r+1]}")

            if maxIdx < l:
                m = max(nums[l:r+1])
                maxIdx = nums.index(m, l, r+1)
                print("m reset")
            
            if nums[r] > m and r >= l:
                maxIdx = r
                m = nums[r]
            print(f"m = {m}\n")

            if (r - l + 1) == k:
                print(f"{m} added to maxarr\n")
                maxArr.append(m)

        return maxArr

            
                