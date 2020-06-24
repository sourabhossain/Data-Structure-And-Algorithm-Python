class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __insert(self, node, val):
        if node is None:
            return
        if node.val == val:
            return
        elif val < node.val:
            if node.left is None:
                node.left = Node(val)
                return
            self.__insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
                return
            self.__insert(node.right, val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert(self.root, val)

    def delete(self):
        pass

    def search(self, val):
        node = self.root

        while node is not None:
            if node.val == val:
                return True
            elif node.val > val:
                node = node.left
            else:
                node = node.right
        return False

    def minimum(self):
        node = self.root

        while node.left:
            node = node.left
        return node.val

    def maximum(self):
        node = self.root

        while node.right:
            node = node.right
        return node.val

    def __preOrder(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.__preOrder(node.left)
        self.__preOrder(node.right)

    def preOrder(self):
        print("Pre-Order:", end=" ")
        self.__preOrder(self.root)
        print()

    def __inOrder(self, node):
        if node is None:
            return
        self.__inOrder(node.left)
        print(node.val, end=" ")
        self.__inOrder(node.right)

    def inOrder(self):
        print("In-Order:", end=" ")
        self.__inOrder(self.root)
        print()

    def __postOrder(self, node):
        if node is None:
            return
        self.__postOrder(node.left)
        self.__postOrder(node.right)
        print(node.val, end=" ")

    def postOrder(self):
        print("Post-Order:", end=" ")
        self.__postOrder(self.root)
        print()

    def __length(self, node):
        if node is None:
            return 0
        return 1 + self.__length(node.left) + self.__length(node.right)

    def __len__(self):
        return self.__length(self.root)


data = [50, 65, 48, 76, 45, 31, 25, 84]
my_tree = BinarySearchTree()

for item in data:
    my_tree.insert(item)

my_tree.preOrder()
my_tree.inOrder()
my_tree.postOrder()
print("Length:", len(my_tree))
print("Minimum:", my_tree.minimum())
print("Maximum:", my_tree.maximum())
print("Search:", my_tree.search(31))
