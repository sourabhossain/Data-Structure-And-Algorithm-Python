class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        vals = []
        node = self.head

        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

    def add(self, val):
        node = Node(val)

        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

    def remove(self, value):
        node = self.head

        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

        self.size -= 1

    def remove_first(self):
        if self.head is not None:
            self.__remove_node(self.head)
            self.size -= 1

    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)
            self.size -= 1


my_list = DoubleLinkedList()

my_list.add(10)
my_list.add(20)
my_list.add(30)
my_list.add(40)
my_list.add(50)

my_list.remove_first()

print(my_list)
print(f"Size: {my_list.size}")
