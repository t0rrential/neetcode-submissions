class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        final = []
        start, end = None, 0

        def inbound(i):
            # print(f"{start} {end}")
            return start <= i and i <= end

        for i in intervals:
            if start == None:
                start = i[0]
                end = i[1]

            else:
                # when to extend start:
                #     start <= i[1] <= end and i[0] < start
                # when to extend end:
                #     start <= i[0] <= end and i[1] > end
                # when to stop:
                #     i[0] > end
                if inbound(i[1]) and i[0] < start:
                    start = i[0]
                if inbound(i[0]) and i[1] > end:
                    end = i[1]
                
                if i[0] > end:
                    final.append([start, end])
                    start = i[0]
                    end = i[1]


        final.append([start, end])

        # print(intervals)
        # print(final)
        return final