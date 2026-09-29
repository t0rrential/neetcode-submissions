class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [ 4 1 0 7 ]
        # [ 2 2 1 1 ]

        # desc:

        # [ 0 1 4 7 ]
        # [ 1 2 2 1 ]

        # (10 - 0) -> (10)/1 = 10
        # (10 - 1) -> (9)/2  = 9
        # (10 - 4) -> (6)/2  = 3
        # (10 - 7) -> (3)/1  = 3

        # simple algo:
        #     sort by desc
        #     find time for each car
        #     in reverse, add times to stack. if curr time < peek time, +1 to fleets

        res = 0
        stack = []
        pairs = [(position[i], speed[i]) for i in range(0, len(speed))]

        pairs.sort(reverse=True)

        print(pairs)

        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            print(f"({target} - {pair[0]}) / {pair[1]} = {time}")
            if len(stack) > 0:
                peek = stack[len(stack) - 1]

                if peek < time:
                    stack.append(time)
            else:
                stack.append(time)
                # first time run needs to populate stack
            print(len(stack))

        return len(stack)