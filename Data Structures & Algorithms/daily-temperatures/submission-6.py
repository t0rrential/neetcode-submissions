class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        n = len(temperatures) - 1
        s = []
        days = [0] * (n + 1)

        # loop with temperatures going in reverse:
        # 1. check top of stack. if the top element is smaller than the current element, pop the top element.
        # repeat this as many times as necessary.
        # 2. if the top of the stack is larger, then update the days array accordingly and push yourself onto the stack.  
        # 3. update the days array for the current position.

        for idx, temp in enumerate(temperatures[::-1]):
            if not s:
                s.append(n)
            else:
                if temperatures[s[-1]] <= temp:
                    while s and temperatures[s[-1]] <= temp:
                        s.pop()
                    if s:
                        days[n - idx] = s[-1] - (n - idx)
                    else:
                        days[n - idx] = 0
                    s.append(n - idx)

                elif temperatures[s[-1]] > temp:
                    days[n - idx] = s[-1] - (n - idx)
                    s.append(n - idx)

        return days


