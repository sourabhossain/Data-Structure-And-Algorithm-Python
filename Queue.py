class Queue:
    def __init__(self):
        self.__list = []

    def enqueue(self, val):
        self.__list.append(val)

    def dequeue(self):
        if len(self.__list) == 0:
            return "Queue is empty!"
        return self.__list.pop(0)

    def front(self):
        if len(self.__list) == 0:
            return "Queue is empty!"
        return self.__list[0]

    def back(self):
        if len(self.__list) == 0:
            return "Queue is empty!"
        return self.__list[-1]

    def is_empty(self):
        if len(self.__list):
            return False
        else:
            return True

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        return f"[{', '.join(str(item) for item in self.__list)}]"


my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.enqueue(50)

my_queue.dequeue()
my_queue.dequeue()

print(my_queue)
print(my_queue.front())
print(my_queue.back())
print(my_queue.is_empty())
print(len(my_queue))
