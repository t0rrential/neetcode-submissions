class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        candidates = set()

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c]:
                    candidates.add((r, c))

        while candidates:
            i = candidates.pop()
            beside = {i} 
            candidates.discard(i)

            area = 1
            while beside:
                curr = beside.pop()
                for c in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    cc = (curr[0] + c[0], curr[1] + c[1])
                    if cc in candidates:
                        candidates.discard(cc)
                        beside.add(cc)
                        area += 1
            
            maxarea = max(maxarea, area)

        return maxarea
        