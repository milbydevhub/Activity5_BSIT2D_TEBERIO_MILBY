class ArrayQueue:
    """Circular queue implementation using a fixed-size Python list."""

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: cannot enqueue into a full queue.")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: there is no front element.")
        return self.data[self.front]

    def __str__(self):
        if self.is_empty():
            return "FRONT -> (empty)"
        items = [str(self.data[(self.front + i) % len(self.data)])
                 for i in range(self.size)]
        return "FRONT -> " + " -> ".join(items) + " <- REAR"
