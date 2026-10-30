class ArrayStack:
    """Stack implementation using a fixed-size Python list."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: cannot push into a full stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: there is no top element.")
        return self.data[self.top]

    def __str__(self):
        if self.is_empty():
            return "[] (empty)"
        return "[" + ", ".join(str(x) for x in self.data[:self.top + 1]) + "] (bottom to top)"
