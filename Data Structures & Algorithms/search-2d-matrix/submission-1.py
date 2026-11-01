class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # 1) find the row that could contain target
        u, d = 0, len(matrix) - 1
        while u <= d:
            row = (u + d) // 2
            if target < matrix[row][0]:
                d = row - 1
            elif target > matrix[row][-1]:
                u = row + 1
            else:
                break
        if u > d:
            return False

        # 2) standard binary search within that row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False