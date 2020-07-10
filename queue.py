
# Queue for breadth first search
class Queue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0
        self.front = 0
        self.back = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def enqueue(self, item):
        if not(self.is_full()):
            self.items[self.back % self.capacity] = item
            self.back += 1
            self.num_items += 1
        else:
            raise IndexError

    def dequeue(self):

        if not(self.is_empty()):
            item = self.items[self.front % self.capacity]
            self.front += 1
            self.num_items -= 1
            return item
        else:
            raise IndexError

    def size(self):
        return self.num_items

