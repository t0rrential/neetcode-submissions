class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        idx = 0
        
        for i in range(0, len(nums)):
            d[nums[i]] = i

        for i in nums:
            test_i = d.get(target - i, False)

            if test_i and test_i != idx:
                return [idx, test_i]

            else:
                idx += 1