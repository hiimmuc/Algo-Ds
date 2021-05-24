# FIFO rules


class Queue:
    def __init__(self, capacity: int):
        self.front = self.size = 0
        self.rear = capacity-1
        self.Q = [None] * capacity
        self.capacity = capacity

    def EnQueue(self, data):
        if self.isFull():
            print('Full!!')
            self.DeQueue()
            self.size += 1
        else:
            self.size += 1
        print('rear:', self.rear, 'front:', self.front, 'size:', self.size)
        if self.rear < self.capacity:
            self.rear = (self.rear + 1) % (self.capacity)
            self.Q[self.rear] = data
        else:
            self.rear = (self.rear + 1) % (self.size)
            self.Q[self.rear] = data

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return
        print('del', self.Q[self.front])

        self.Q[self.front] = None
        self.front = (self.front + 1) % (self.capacity)
        self.size -= 1

    def el_front(self):
        if self.isEmpty():
            return None
        return self.Q[self.front]

    def el_rear(self):
        if self.isEmpty():
            return None
        return self.Q[self.rear]

    def size(self) -> int:
        c = 0
        for x in self.Q:
            if x is None:
                return c
            c += 1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def print(self):
        print('>> Queue Element: ')
        s = ''
        for i in range(self.front, self.rear + 1):
            s += f"|{self.Q[i]}| "
        print('Front->' + s + '<-Rear')


if __name__ == "__main__":
    q1 = Queue(9)
    for x in range(10):
        q1.EnQueue(x)
    q1.print()
    print(q1.el_front())
    print(q1.el_rear())

# check again the EnQueue amd DeQueue
