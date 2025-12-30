class MyQueue:

    def __init__(self):
        # s1 acts as the input container
        self.s1 = []
        # s2 acts as the output container
        self.s2 = []

    def push(self, x: int) -> None:
        # Simply push to the input stack
        self.s1.append(x)

    def pop(self) -> int:
        # Ensure s2 has the current oldest elements
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        # If s2 is empty, move everything from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks have no elements
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()