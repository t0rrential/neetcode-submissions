class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            
            if l < r:
                while l < r:
                    target = -nums[l] + -nums[r]

                    if target > n:
                        l += 1

                    elif target < n:
                        r -= 1
                    
                    target = -nums[l] + -nums[r]

                    if target == n and l < r and l != i:
                        test = [n, nums[l], nums[r]]
                        sol.append(test)

                        l += 1
                        r -= 1

                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return sol
            