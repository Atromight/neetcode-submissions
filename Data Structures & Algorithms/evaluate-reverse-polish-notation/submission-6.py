class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                y = stack.pop()
                x = stack.pop()
                print(x, token, y)


                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                elif token == "*":
                    stack.append(x * y)
                elif token == "/":
                    stack.append(int(x / y))
            # if token is str(int)
            else:
                num = int(token)
                stack.append(num)

        return stack.pop()
        