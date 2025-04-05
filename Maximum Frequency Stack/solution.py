from collections import deque

class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
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
            self.group[f] = deque()

        self.group[f].append(val)
        self.max_freq = max(self.max_freq, f)


    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -=1
        if not self.group[self.max_freq]:
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()