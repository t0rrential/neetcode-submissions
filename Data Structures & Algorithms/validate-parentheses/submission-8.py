class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oepen = {"(": ")",
                 "{": "}",
                 "[": "]"}
                
        close = {")": "(",
                 "}": "{",
                 "]": "["}

        for b in s:
            if b in oepen:
                stack.append(b)
            elif b in close:
                if stack:
                    if stack[-1] == close[b]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        print(stack)
        if stack:
            return False
        else:
            return True