class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': lambda a, b: a + b, 
                     '-': lambda a, b: a - b,
                     '*': lambda a, b: a * b,
                     '/': lambda a, b: int(a / b)}
        s = []

        for i in tokens:
            if i.replace("-", "").isnumeric():
                s.append(int(i))
            else:
                if i in operators:
                    operation = operators[i]

                    a2 = s.pop()
                    a1 = s.pop()

                    s.append(operation(a1, a2))
            print(s)

        return s.pop()
