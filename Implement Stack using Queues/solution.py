class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class MyStack(object):

    def __init__(self):
        self.head = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.head = Node(x, self.head)

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            raise ValueError('Stack is empty')
        item = self.head.item
        self.head = self.head.next
        return item

    def top(self):
        """
        :rtype: int
        """
        return self.head.item

    def empty(self):
        """
        :rtype: bool
        """
        return self.head is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()