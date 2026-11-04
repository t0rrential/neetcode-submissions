class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for st in strs:
            h = [0 for i in range(26)]
            for i in st:
                h[ord(i) - 97] += 1

            d[tuple(h)].append(st)
        
        return [l for l in d.values()]
            

                
