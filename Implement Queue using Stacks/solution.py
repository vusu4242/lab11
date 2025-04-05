class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class MyQueue(object):

    def __init__(self):
        self.tail = None
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.head:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        else:
            self.tail = Node(x)
            self.head = self.tail


    def pop(self):
        """
        :rtype: int
        """
        if self.head:
            item = self.head.item
            self.head = self.head.next
            return item
        raise ValueError('Oueue is empty')

    def peek(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self.head.item


    def empty(self):
        """
        :rtype: bool
        """
        return self.head is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()