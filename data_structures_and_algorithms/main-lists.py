from lists.linked_list import LinkedList

list = LinkedList()

while True:
    print('Menu de opcoes:')
    print('1  - Inserir elemento inicio')
    print('2  - Inserir elemento final')
    print('3  - Inserir elemento (qualquer posicao)')
    print('4  - Remover elemento inicio')
    print('5  - Remover elemento final')
    print('6  - Remover elemento (qualquer)')
    print('7  - Obter quantidade de elementos na lista')
    print('8  - Obter elemento pelo indice')
    print('9  - Obter indice pelo elemento')
    print('10 - Alterar elemento')
    print('11 - Impirmir lista')
    print('12 - Limpar lista')
    option = int(input('Opcao: '))

    if option == 1:

        el = int(input('\nDigite o elemento a ser inserido: '))
        list.insert(0, el)

        print(f'\n{list}\n')

    elif option == 2:

        el = int(input('\nDigite o elemento a ser inserido: '))
        list.append(el)

        print(f'\n{list}\n')

    elif option == 3:

        el = int(input('\nDigite o elemento a ser inserido: '))
        index = int(input('\nDigite o indice do novo elemento: '))

        list.insert(index, el)

        print(f'\n{list}\n')

    elif option == 4:

        if len(list) > 0:

            list.remove(list[0])

            if len(list) == 0:
                print('\nA lista esta vazia!\n')

            else:
                print(f'\n{list}\n')

        else:
            print('\nA lista esta vazia!\n')

    elif option == 5:

        if len(list) > 0:
            list.pop()

            if len(list) == 0:
                print('\nA lista esta vazia!\n')

            else:
                print(f'\n{list}\n')

        else:
            print('\nA lista esta vazia!\n')

    elif option == 6:

        if len(list) > 0:

            el = int(print('\nDigite o elemento a ser removido: '))
            list.remove(el)

            if len(list) == 0:
                print('\nA lista esta vazia!\n')

            else:
                print(f'\n{list}\n')

        else:
            print('\nA lista esta vazia!\n')

    elif option == 7:

        if len(list) == 0:
            print('\nA lista esta vazia!\n')

        else:
            print(f'\nQuantidade de elementos na lista: {len(list)}')

    elif option == 8:

        index = int(print("\nDigite o indice: "))
        el = list[index]

        print(f'\nElemento na posicao {index}: {el}')

    elif option == 9:

        el = int(print("\nDigite o elemento: "))
        index = list.index(el)

        print(f'\nElemento na posicao {index}: {el}')

    elif option == 10:

        index = int(print("\nDigite o indice do elemento a ser alterado: "))
        el = int(print("Digite o novo elemento: "))

        list[index] = el

        if list[index] == el:
            print('\nAlteracao realizada com sucesso!\n')
            print(list)

        else:
            print('\nHouve um erro na alteracao!')

    elif option == 11:

        if len(list) == 0:
            print('\nA lista esta vazia!\n')

        else:
            print(f'\n{list}\n')

    elif option == 12:

        list.clear()

        if len(list) == 0:
            print('\nA lista esta vazia!\n')

    else:
        print("\nOpcao Invalida!")

# list.append(7)
# print(len(list))  # 1
# # print(list)  # IndexError: the lis is empty

# list.append(80)
# print(len(list))  # 2
# print(list[0])  # 7

# list[1] = 56
# print(list[0])  # 7
# print(list[1])  # 56
# print(len(list))  # 2

# print(list.index(7))  # 0
# # print(list.index(80))  # ValueError: 80 is not in the list
# print(list.index(56))  # 1

# list.clear()
# print(len(list))  # 0
# # print(list[0]) # list index out of range

# list.append(7)
# list.append(80)
# list.append(56)
# list.append(32)
# list.append(17)
# print(list) # 7 -> 80 -> 56 -> 32 -> 17 ->

# list.insert(0, 22)
# print(list[0])  # 22
# print(list[len(list) - 1])  # 17
# # print(list[10]) # IndexError: list index out of range

# print(list) # 22 -> 7 -> 80 -> 56 -> 32 -> 17 ->
# list.remove(22)
# list.remove(7)
# print(list)  # 80 -> 56 -> 32 -> 17 ->
# list.remove(80)
# list.remove(56)
# list.remove(32)
# list.remove(17)
# # print(list) # IndexError: the list is empty
