class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == "(" or s[i] == "*":
                stack.append(s[i])

            elif s[i] == ")":
                if not stack:
                    return False

                if stack and stack[-1] == "(":
                    stack.pop()

                elif stack and stack[-1] != "(": # i.e. stack[-1] == "*"
                    stars = 0
                    while stack and stack[-1] != "(":
                        stack.pop()
                        stars += 1

                    if stack:
                        stack.pop()

                    else:
                        if stars > 0:
                            stars -= 1
                        else:
                            return False

                    for star in range(stars):
                        stack.append("*")

        if stack:
            stars = 0
            parenth = 0
            m = len(stack)
            for i in range(m-1, -1, -1):
                char = stack[i]
                if char == "(":
                    if stars > 0:
                        stars -= 1

                    else: # stars == 0
                        return False

                elif char == "*":
                    stars += 1

        return True
