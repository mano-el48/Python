from models.node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def __len__(self):
        return self._length

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

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.el
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, el):
        pointer = self._getNode(index)
        if pointer:
            pointer.el = el
        else:
            raise IndexError('list index out of range')

    def index(self, el):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.el == el:
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

    def remove(self, el):
        if self.head == None:
            raise ValueError('{} is not in the list'.format(el))

        elif self.head.el == el:
            self.head = self.head.next
            self._length -= 1
            return True

        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.el == el:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._length -= 1
            return True

    def clear(self):
        self.head = None
        self._length = 0

    def __repr__(self):
       pointer = self.head
       if pointer == None:
           raise IndexError('the list is empty')
       r = ""
       pointer = self.head
       while(pointer):
           r = r + str(pointer.el) + " -> "
           pointer = pointer.next
       return r
    
    def __str__(self):
        return self.__repr__()