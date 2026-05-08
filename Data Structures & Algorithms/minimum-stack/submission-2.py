class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = None
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.stack_min = val
        else:
            encoded_val = val - self.stack_min
            self.stack.append(encoded_val)
            if val < self.stack_min:
                self.stack_min = val
        

    def pop(self) -> None:
        encoded_val = self.stack.pop()
        if encoded_val < 0:
            self.stack_min -= encoded_val


    def top(self) -> int:
        encoded_val = self.stack[-1]
        if encoded_val >= 0:
            return encoded_val + self.stack_min
        else:
            return self.stack_min
        

    def getMin(self) -> int:
        return self.stack_min
        
