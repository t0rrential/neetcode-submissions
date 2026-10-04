class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        s = numbers[l] + numbers[r]

        while s != target:
            s = numbers[l] + numbers[r]

            if s > target:
                r -= 1
            elif s < target:
                l += 1

        return [l + 1, r + 1]
