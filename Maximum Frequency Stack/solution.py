from collections import deque

class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val:int):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freq:
            self.freq[val]+=1
        else:
            self.freq[val] = 1

        f = self.freq[val]

        if not f in self.group:
            self.group[f] = deque

        self.group[val].append(val)
        self.max_freq = max(self.max_freq, f)


    def pop(self):
        """
        :rtype: int
        """
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()