from modules.node import Node

class LinkeList:
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

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, el):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        if pointer:
            pointer.data = el
        else:
            raise IndexError('list index out of range')

    def indexOf(self, el):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == el:
                return i
            pointer = pointer.next
            i += 1

        raise ValueError('{} is not in the list'.format(el))


list = LinkeList()
print(len(list))  # 0

list.append(7)
print(len(list))  # 1
print(list[0])  # 7

list.append(80)
print(len(list))  # 2
print(list[1])  # 80
# print(list[2])  # IndexError: list index out of range

list[1] = 56
print(list[1])  # 56

print(list.indexOf(7))
# print(list.indexOf(80))  # ValueError: 80 is not in the list
print(list.indexOf(56))
