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

    def get(self, index):
        pass

    def set(self, index, el):
        pass
    
    def __getitem__(self, index):
        pass
    
    def __setitem__(self, index):
        pass



list = LinkeList()
print(len(list))

list.append(7)
print(len(list))

list.append(80)
print(len(list))
