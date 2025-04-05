class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class FreqStack(object):

    def __init__(self):
        self.head = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.head = Node(val, self.head)


    def pop(self):
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()