from lists.linked_list import LinkedList

list = LinkedList()
list.append(7)
print(len(list))  # 1
# print(list)  # IndexError: the lis is empty

list.append(80)
print(len(list))  # 2
print(list[0])  # 7

list[1] = 56
print(list[0])  # 7
print(list[1])  # 56
print(len(list))  # 2

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
print(list) # 7 -> 80 -> 56 -> 32 -> 17 ->

list.insert(0, 22)
print(list[0])  # 22
print(list[len(list) - 1])  # 17
# print(list[10]) # IndexError: list index out of range

print(list) # 22 -> 7 -> 80 -> 56 -> 32 -> 17 ->
list.remove(22)
list.remove(7)
print(list)  # 80 -> 56 -> 32 -> 17 ->
list.remove(80)
list.remove(56)
list.remove(32)
list.remove(17)
# print(list) # IndexError: the list is empty