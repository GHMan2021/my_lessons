class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2:
            return 0
        elif v1 < v2:
            return -1
        else:
            return 1

    def add(self, value):

        if self.head is None:
            self.head = Node(value)
            Node(value).prev = None
            Node(value).next = None
            self.tail = Node(value)
            return

        if self.__ascending:
            result_compared = -1
        else:
            result_compared = 1

        v1 = self.head
        v2 = Node(value)
        if self.compare(v1.value, v2.value) != result_compared:
            v2.prev = v1.prev
            v2.next = v1
            v1.prev = v2
            self.head = v2
            self.tail = v1
            return

        v1 = self.tail
        if self.compare(v1.value, v2.value) == result_compared:
            v2.prev = v1
            v2.next = v1.next
            v1.next = v2
            self.tail = v2
            self.head = v1
            return

        for i in range(1, self.len()):
            v1 = self.get_all()[i]
            if self.compare(v1.value, v2.value) != result_compared:
                v1.prev.next = v2
                v2.prev = v1.prev
                v2.next = v1
                v1.prev = v2
                return

    def find(self, val):
        node = self.head
        if node is None:
            return None
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def delete(self, val):
        node = self.find(val)

        if node is None:
            return

        if self.len() == 1:
            asc = self.__ascending
            return self.clean(asc)

        if node == self.head:
            node.next.prev = None
            self.head = node.next
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.__init__(asc)

    def len(self):
        return len(self.get_all())

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1.strip()
        v2.strip()
        if v1 == v2:
            return 0
        elif v1 < v2:
            return -1
        else:
            return 1
