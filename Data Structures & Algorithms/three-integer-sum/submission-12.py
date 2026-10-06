class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        sol = set()

        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            # print(f"l = {nums[l]}, r = {nums[r]}, n = {n}")
            if l < r:
                target = -nums[l] + -nums[r]
                valid = 0
                while l < r:
                    if target > n:
                        l += 1

                    elif target < n:
                        r -= 1
                    
                    target = -nums[l] + -nums[r]

                    if target == n and l < r and l != i:
                        test = [n, nums[l], nums[r]]
                        # print(f"sum({test}) = {sum(test)}")

                        if sum(test) == 0:
                            sol.add(tuple(test))

                        l += 1
        return [list(x) for x in sol]
            