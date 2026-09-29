class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        idx = 0

        for i in range(len(nums)):
            d[nums[i]] = i

        for i in nums:
            tt = target

            if d.get(tt - i, False) != False and idx != d.get(tt - i, False):
                return [idx, d[tt - i]]
            else:
                idx = idx + 1
