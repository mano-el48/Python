from modules.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def append(self, el):
        if self.head:
            # inerção quando a lista ja possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(el)

        else:
            # primeira inserção
            self.head = Node(el)
        self._length += 1

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
        return pointer

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, el):
        pointer = self._getNode(index)
        if pointer:
            pointer.data = el
        else:
            raise IndexError('list index out of range')

    def index(self, el):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == el:
                return i
            pointer = pointer.next
            i += 1

        raise ValueError('{} is not in the list'.format(el))

    def insert(self, index, el):
        node = Node(el)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._length += 1
    
    def remove(self):
        pass

    def clear(self):
        self.head = None
        self._length = 0
    
    def toString(self):
        pass



list = LinkedList()
print(len(list))  # 0

list.append(7)
print(len(list))  # 1
print(list[0])  # 7

list.append(80)
print(len(list))  # 2
print(list[1])  # 80

list[1] = 56
print(list[1])  # 56

print(list.index(7))  # 0
# print(list.index(80))  # ValueError: 80 is not in the list
print(list.index(56))  # 1

list.clear()
print(len(list))  # 0
# print(list[0]) # list index out of range

list.append(7)
list.append(80)
list.append(56)
list.append(32)
list.append(17)

list.insert(0, 22)
print(list[0])  # 22 -> head
print(list[len(list) - 1]) # 17
# print(list[10]) # IndexError: list index out of range
