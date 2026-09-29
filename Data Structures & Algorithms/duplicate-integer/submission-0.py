class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)

        if len(setNums) != len(nums):
            return True

        return False