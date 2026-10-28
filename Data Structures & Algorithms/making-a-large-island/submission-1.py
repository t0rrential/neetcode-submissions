class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # hi = seen island set, coord : island id
        # k = id : size
        # wl = dfs check over
        # nk = unused

        hi = {}
        k = {}
        zeros = set()

        fuckyou = 1
        n = len(grid)
        id = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] and (i, j) not in hi:
                    # candidacy
                    wl = {(i, j)}
                    hi[(i, j)] = id
                    l = 1

                    while wl:
                        w = wl.pop()
                        wi, wj = w

                        if wj < n - 1: # right 
                            if grid[wi][wj+1] and (wi, wj+1) not in hi:
                                wl.add((wi, wj+1))
                                hi[(wi, wj+1)] = id
                                l += 1

                        if wj > 0: # left 
                            if grid[wi][wj-1] and (wi, wj-1) not in hi:
                                wl.add((wi, wj-1))
                                hi[(wi, wj-1)] = id
                                l += 1

                        if wi > 0: # up 
                            if grid[wi-1][wj] and (wi-1, wj) not in hi:
                                wl.add((wi-1, wj))
                                hi[(wi-1, wj)] = id
                                l += 1

                        if wi < n - 1: # down 
                            if grid[wi+1][wj] and (wi+1, wj) not in hi:
                                wl.add((wi+1, wj))
                                hi[(wi+1, wj)] = id
                                l += 1
                        
                    if l:
                        k[id] = l
                        id += 1
                elif not grid[i][j]:
                    zeros.add((i, j))

        if not zeros:
            return n * n

        while zeros:
            candidate = zeros.pop()
            wi, wj = candidate
            si = set()
            tl = 1

            if wj < n - 1: # right 
                if grid[wi][wj+1]:
                    ci = hi[(wi, wj+1)]
                    if ci not in si:
                        si.add(ci)
                        tl += k[ci]

            if wj > 0: # left 
                if grid[wi][wj-1]:
                    ci = hi[(wi, wj-1)]
                    if ci not in si:
                        si.add(ci)
                        tl += k[ci]

            if wi > 0: # up 
                if grid[wi-1][wj]:
                    ci = hi[(wi-1, wj)]
                    if ci not in si:
                        si.add(ci)
                        tl += k[ci] 


            if wi < n - 1: # down 
                if grid[wi+1][wj]:
                    ci = hi[(wi+1, wj)]
                    if ci not in si:
                        si.add(ci)
                        tl += k[ci]

            fuckyou = max(fuckyou, tl)

        return fuckyou


            
