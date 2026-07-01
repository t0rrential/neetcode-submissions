class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = defaultdict(int)

        for n in nums:
            if hm[n] > 0:
                return True

            else:
                hm[n] += 1
        
        return False
