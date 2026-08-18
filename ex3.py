
### Q3.1

class Node:
    def __init__(self, element):  # header->node(data maintained in the node)->pointer->next node
        self.element = element
        self.next = None


class LinkedList:  # chain of nodes
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def addLast(self, e):
        newNode = Node(e)

        if self.__tail is None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next

        self.__size += 1

    def getSize(self):
        return self.__size

    def to_list(self):
        result = []
        current = self.__head
        while current is not None:
            result.append(current.element)
            current = current.next
        return result

    def LinkedListBubbleSort(linkListToSort):

        size = linkListToSort.getSize()

        if size <= 1:
            return

        swapped = True  # swapped occurred
        while swapped:
            swapped = False  # assumes list is sorted
            current = linkListToSort.__head

            while current.next is not None:

                if current.element > current.next.element:
                    current.element, current.next.element = current.next.element, current.element
                    swapped = True  # another swapped occurred, list needs to be checked again
                current = current.next

        return linkListToSort



