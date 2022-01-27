class Node:
    def __init__(self, value, link = None):
        #set data and link for Node
        self.data = value
        self.link = link

    def value(self):
        return self.data

    def next(self):
        return self.link


class LinkedList:
    def __init__(self, values=[]):
        #First node in list
        self.head_node = None

        #Input list to linked list
        self.values = values
        self.length = 0
        for value in self.values:
            self.push(value)

    def __iter__(self):
        if len(self) == 0:
            return []
        count = self.length
        iter_node = self.head_node
        while count != 0:
            yield iter_node.value()
            iter_node = iter_node.next()
            count -= 1

    def __len__(self):
        return self.length

    #curr head of list
    def head(self):
        if len(self) == 0:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        node = Node(value)
        if self.head_node == None:
            self.head_node = node
        else:
            node.link = self.head_node
            self.head_node = node
        self.length += 1

    def pop(self):
        if len(self) == 0:
            raise EmptyListException("The list is empty.")
        x = self.head_node.value()
        self.head_node = self.head_node.next()
        self.length -= 1
        return x

    def reversed(self):
        rev = []
        for value in self:
            rev.insert(0, value)
        return rev


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message