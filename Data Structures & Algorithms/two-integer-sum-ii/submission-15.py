class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        sol = []
        l, r = 0, length-1

        while l < r:
            ssum = numbers[l] + numbers[r]

            if ssum == target:
                sol = [l+1, r+1]
                break
            if ssum > target:
                r -= 1
            if ssum < target:
                l += 1

        return sol
