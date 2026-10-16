class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        possible = set()
        islands = 0

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == "1":
                    possible.add((r,c))

        while possible:
            # print(possible)
            can = possible.pop()
            adj = {can}
            
            while adj:
                candidate = adj.pop()

                r, c = candidate
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    n = (r + dr, c + dc)
                    if n in possible:
                        adj.add(n)
                        possible.discard(n)
            islands += 1
        
        return islands



        

