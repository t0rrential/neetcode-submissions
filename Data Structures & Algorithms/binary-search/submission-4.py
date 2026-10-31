class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        def bst(s, e):
            i = (e - s + 1) // 2
            print(f"nums[{s}:{e}+1] = {nums[s:e+1]}, where i = {i}")
            # print(nums[i])

            if nums[s + i] == target:
                return s + i

            if i <= 1:
                if nums[s] == target:
                    return s
                if nums[e] == target:
                    return e
                return -1

            if nums[s + i] > target:
                return bst(s, s + i)

            if nums[s + i] < target:
                return bst(e - i, e)

            
        return bst(0, len(nums) - 1)
