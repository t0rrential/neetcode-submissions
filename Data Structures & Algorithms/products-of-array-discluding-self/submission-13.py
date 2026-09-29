class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nl = len(nums)
        f, b, r = [1] * nl, [1] * nl, []
        f[0] = nums[0]
        b[0] = nums[-1]

        # print(f"f {f}")
        # print(f"b {b}")

        for i, n in enumerate(nums[1:]):
            f[i + 1] = n * f[i]

        # print(nums[:0:-1])

        for i, n in enumerate(nums[-2::-1]):
            b[i+1] = b[i] * n
        b = b[::-1]
 

        # print(f"f {f}")
        # print(f"b {b}")

        for i in range(nl):
            bI = i + 1
            fI = i - 1

            nums[i] = (f[fI] if fI >= 0 else 1) * (b[bI] if bI < nl else 1)
            
        return nums