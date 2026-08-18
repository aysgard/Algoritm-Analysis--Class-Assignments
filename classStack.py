
### Q2.1

class Stack:
    def __init__(self):
        self.__elements = []

    def isEmpty(self):
        return len(self.__elements) == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements.pop()

    def getSize(self):
        return len(self.__elements)

    def findMin(self):
        if self.isEmpty():
            return None
        else:
            return min(self.__elements)

    def reverse(self):

        new_stack = Stack()

        for item in reversed(self.__elements):
            new_stack.push(item)

        return new_stack

