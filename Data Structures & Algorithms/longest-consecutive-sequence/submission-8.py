class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0

        longest = []
        count = 1
        nums = sorted(list(set(nums)))
        length = len(nums)

        for i in range(0, length):
            if i+1 < length:
                if nums[i+1] - nums[i] == 1:
                    count += 1
                else:
                    longest.append(count)
                    count = 1
        longest.append(count)

        longest = sorted(longest, reverse=True)           
        return longest[0]      