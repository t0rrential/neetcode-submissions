class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        coderotted = deque([])
        fresh = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    coderotted.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while coderotted:
            i, j = coderotted.popleft()
            # grid[i][j] = 0

            if i > 0 and grid[i - 1][j] == 1:
                grid[i-1][j] += grid[i][j] 
                fresh -= 1
                coderotted.append((i-1, j))

            if j > 0 and grid[i][j - 1] == 1:
                grid[i][j-1] += grid[i][j] 
                fresh -= 1
                coderotted.append((i, j-1))

            if m - 1 > j and grid[i][j + 1] == 1:
                grid[i][j+1] += grid[i][j] 
                fresh -= 1
                coderotted.append((i, j+1))

            if n - 1 > i and grid[i + 1][j] == 1:
                grid[i+1][j] += grid[i][j] 
                fresh -= 1
                coderotted.append((i+1, j))

        [print(r) for r in grid]

        if fresh:
            return -1
        else:
            return max(grid[i][j] - 2, 0)