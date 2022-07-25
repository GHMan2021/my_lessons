class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        if node is None:
            return None
        while node is not None:
            if node.value == val:
                return node
            node = node.next

    def find_all(self, val):
        node = self.head
        finded_list = []
        while node is not None:
            if node.value == val:
                finded_list.append(node)
            node = node.next
        return finded_list

    def delete(self, val, all=False):
        node = self.head
        if node is None:
            return

        while node is not None:
            if node.value == val:
                if node.prev is None:
                    if node.next is None:
                        self.__init__()
                        return
                    else:
                        self.head = node.next
                        node.next.prev = None
                else:
                    if node.next is None:
                        self.tail = node.prev
                        node.prev.next = None
                        return
                    else:
                        node.prev.next = node.next
                        node.next.prev = node.prev
                if all == False:
                    return
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        node = self.head
        count = 0
        if node is None:
            return count
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        if all([afterNode is None, self.head is None]):
            self.add_in_head(newNode)
        elif all([afterNode is None, self.head is not None]):
            self.add_in_tail(newNode)
        else:
            if afterNode == self.tail:
                self.add_in_tail(newNode)
            else:
                newNode.next = afterNode.next
                newNode.prev = afterNode
                afterNode.next = newNode
                afterNode.next.prev = newNode

    def add_in_head(self, newNode):
        node = self.head
        if node is None:
            newNode.prev = None
            newNode.next = None
            self.tail = newNode
        else:
            newNode.next = node
            newNode.prev = None
            node.prev = newNode
        self.head = newNode
