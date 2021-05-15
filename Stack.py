from Node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print(self):
        if(self.length == 0):
            return print('Stack is empty.')
        n = self.bottom
        node_text = ''
        while n is not None:
            node_text += f' {n.value} -'
            n = n.next
        print(f"[{node_text.rstrip(' -')} ]")

    def peak(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if(self.length == 0):
            self.bottom = new_node
            self.top = new_node
            self.length += 1
            return
        self.top.next = new_node
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return print('Stack is empty.')
        n = self.bottom
        if n.next is None:
            self.bottom = None
            self.top = None
            self.length -= 1
        for x in range(self.length-2):
            n = n.next
        n.next = None
        self.top = n
        self.length -= 1
