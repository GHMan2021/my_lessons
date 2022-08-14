class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)
