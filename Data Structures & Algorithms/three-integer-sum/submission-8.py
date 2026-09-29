class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3:
            return []

        output = set()
        nums = sorted(nums)

        print(f"sorted nums: {nums}")

        # -4 -1 -1 0 1 2

        # -4 -3 -2 -1 0 1 2 3 5 6
        #  ^  ^                 ^
        #  t  l                 r
        # b/c -t    l + r
        #      4 > -3 + 6
        # move l to right 1 as it's too small

        # -4 -2 6

        for idx, elem in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            # want to see if any pair has target = -elem
            target = -elem

            if idx <= length - 3:
                l, r = idx + 1, length - 1 

                while l < r:
                    print(f"target: {target}, l = {nums[l]}, r = {nums[r]}")
                    summed = nums[l] + nums[r]
                    
                    if summed == target:
                        output.add((elem, nums[l], nums[r]))
                        l += 1
                        r -= 1

                    if summed > target:
                        # sum is larger than target
                        r -= 1

                    if summed < target:
                        # sum is smaller than target
                        l += 1

        return [list(l) for l in output]