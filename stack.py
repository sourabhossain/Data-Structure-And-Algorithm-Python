class Stack:
    def __init__(self):
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        if len(self.__list) == 0:
            return "Stack is empty!"
        self.__list.pop(0)

    def front(self):
        if len(self.__list) == 0:
            return "Stack is empty!"
        return self.__list[0]

    def back(self):
        if len(self.__list) == 0:
            return "Stack is empty!"
        return self.__list[-1]

    def is_empty(self):
        if len(self.__list):
            return False
        return True

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        return f"[{', '.join(str(item) for item in self.__list)}]"


my_stack = Stack()

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)

my_stack.pop()
my_stack.pop()

print(my_stack)
print(len(my_stack))
