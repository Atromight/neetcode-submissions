class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        for char in s:
            if char in set(["(", "{", "["]):
                char_stack.append(char)
            
            elif char == ")":
                if char_stack:
                    last_char = char_stack.pop()
                    if last_char != "(":
                        return False
                else:
                    return False

            elif char == "}":
                if char_stack:
                    last_char = char_stack.pop()
                    if last_char != "{":
                        return False
                else:
                    return False

            elif char == "]":
                if char_stack:
                    last_char = char_stack.pop()
                    if last_char != "[":
                        return False
                else:
                    return False

        if char_stack:
            return False
        else:
            return True

        