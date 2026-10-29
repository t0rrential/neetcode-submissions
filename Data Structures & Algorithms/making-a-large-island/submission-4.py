class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # solve optimized with claude

        n = len(grid)
        k = [0, 0]  # k[id] = island size; ids start at 2 so they don't clash with 0/1
        id = 2

        # Pass 1: label each island in place and record its size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = id
                    wl = [(i, j)]
                    l = 1
                    while wl:
                        wi, wj = wl.pop()
                        if wj < n - 1 and grid[wi][wj+1] == 1:  # right
                            grid[wi][wj+1] = id
                            wl.append((wi, wj+1))
                            l += 1
                        if wj > 0 and grid[wi][wj-1] == 1:  # left
                            grid[wi][wj-1] = id
                            wl.append((wi, wj-1))
                            l += 1
                        if wi > 0 and grid[wi-1][wj] == 1:  # up
                            grid[wi-1][wj] = id
                            wl.append((wi-1, wj))
                            l += 1
                        if wi < n - 1 and grid[wi+1][wj] == 1:  # down
                            grid[wi+1][wj] = id
                            wl.append((wi+1, wj))
                            l += 1
                    k.append(l)
                    id += 1

        # Covers the all-ones grid (no zeros to flip)
        best = max(k)

        # Pass 2: try flipping each zero
        for i in range(n):
            row = grid[i]
            for j in range(n):
                if row[j] == 0:
                    s = []
                    if j < n - 1 and row[j+1]:
                        s.append(row[j+1])
                    if j > 0 and row[j-1] and row[j-1] not in s:
                        s.append(row[j-1])
                    if i > 0 and grid[i-1][j] and grid[i-1][j] not in s:
                        s.append(grid[i-1][j])
                    if i < n - 1 and grid[i+1][j] and grid[i+1][j] not in s:
                        s.append(grid[i+1][j])

                    tl = 1
                    for c in s:
                        tl += k[c]
                    if tl > best:
                        best = tl

        return best