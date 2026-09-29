class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backwards = []
        fin = []
        length = len(nums)

        for i in range(0, length):
            forward.append(nums[i] * (forward[i-1] if i - 1 >= 0 else 1))
            backwards.insert(0, nums[length - i - 1] * (backwards[0] if 0 < i else 1))

        for i in range(0, length):
            fin.append((forward[i - 1] if i > 0 else 1) * (backwards[i + 1] if i < length - 1 else 1))

        return fin