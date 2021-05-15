from Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print(self):
        if(self.length == 0):
            return print('Queue is empty.')
        n = self.first
        node_text = ''
        while n is not None:
            node_text += f' {n.value} -'
            n = n.next
        print(f"[{node_text.rstrip(' -')} ]")

    def peek(self):
        if(self.length == 0):
            return print('Queue is empty.')
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.last = new_node
            self.first = new_node
            self.length += 1
            return
        self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        if(self.length == 0):
            return print('Queue is empty.')
        if(self.length == 1):
            self.last = None
        self.first = self.first.next
        self.length -= 1
