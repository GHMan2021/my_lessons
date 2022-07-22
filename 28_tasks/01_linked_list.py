class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        finded_list = []
        if node is None:
            return finded_list
        while node is not None:
            if node.value == val:
                finded_list.append(node)
            node = node.next
        return finded_list

    def delete(self, val, all=False):
        node = self.head
        last_node = None
        if node is None:
            return
        while node is not None:
            if node.value == val:
                if last_node is None:
                    self.head = node.next
                else:
                    last_node.next = node.next
                if node == self.tail:
                    self.tail = last_node
                if all is False:
                    return
            else:
                last_node = node
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
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.find(afterNode.value)
        newNode.next = node.next
        node.next = newNode
