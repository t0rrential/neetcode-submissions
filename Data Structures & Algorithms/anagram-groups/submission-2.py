class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            st = str(set(s))
            if len(s) != len(st):
                st = str(sorted(s))

            d[st].append(s)

        return list(dict(d).values())
            

                
