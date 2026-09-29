class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for i in nums:
            hm[i] += 1

        return sorted(set(nums), key=lambda a: hm[a], reverse=True)[:k]