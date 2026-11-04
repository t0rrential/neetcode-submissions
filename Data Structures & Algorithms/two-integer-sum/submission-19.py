class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, x in enumerate(nums):
            if target - x in hash_table:
                return [hash_table[target - x], i]
            hash_table[x] = i
        
        return None