# stack data structure
# LIFO or FILO rule


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self) -> int:
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self) -> None:
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        pass

    def printStack(self) -> None:
        print('Elements in stack are: ')
        for x in self.stack[len(self.stack)::-1]:
            print(x)


if __name__ == "__main__":
    stacks = Stack()
    # push value
    # for i in range(1, 10):
    #     llist.push(i)
    # append value
    for i in range(10):
        stacks.push(i ** 2)
    stacks.printStack()
    for i in range(10):
        print('pop', stacks.pop())
    print('empty: ', stacks.isEmpty())
