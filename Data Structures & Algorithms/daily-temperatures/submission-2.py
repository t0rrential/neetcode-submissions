class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        # alg:
        # go through list of temps one by one.
        # if tempsStack[i-1] < temps
        # meaning if the number behind temps in the stack is smaller than the current element
        # pop all elements smaller than element and update result using indices

        for idx, ele in enumerate(temperatures):
            if len(stack) > 0:
                peek = stack[len(stack)-1]
                print(f"peek = {temperatures[peek]}, curr ele = {ele}")

                while temperatures[peek] < ele:
                    print(f"t[p] < ele, popping stack")
                    prev = stack.pop()
                    print(f"stack now {stack}, adding {idx} - {prev} to res")
                    result[prev] = abs(idx - prev)
                    print(f"result now {result}")

                    if len(stack) > 0:
                        peek = stack[len(stack) - 1]
                    else:
                        break
    
            stack.append(idx) 

            print(f"s: {stack}\nr: {result}\n")
        print(result)
        return result
