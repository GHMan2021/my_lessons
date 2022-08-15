class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        return self.deque.insert(0, item)

    def addTail(self, item):
        return self.deque.append(item)

    def removeFront(self):
        if not self.deque:
            return None
        return self.deque.pop(0)

    def removeTail(self):
        if not self.deque:
            return None
        return self.deque.pop()

    def size(self):
        return len(self.deque)
