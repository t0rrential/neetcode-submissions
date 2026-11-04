class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        final = []
        start, end = None, 0

        def inbound(i):
            return start <= i and i <= end

        for i in intervals:
            if start == None:
                start = i[0]
                end = i[1]

            else:
                if inbound(i[1]) and i[0] < start:
                    start = i[0]
                if inbound(i[0]) and i[1] > end:
                    end = i[1]
                
                if i[0] > end:
                    final.append([start, end])
                    start = i[0]
                    end = i[1]

        final.append([start, end])
        return final