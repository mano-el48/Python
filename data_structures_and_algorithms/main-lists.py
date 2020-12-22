from lists.linked_list import LinkedList

list = LinkedList()

while True:
    print('\nMenu de opcoes:')
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

        print(f'\n{list}')

    elif option == 2:

        el = int(input('\nDigite o elemento a ser inserido: '))
        list.append(el)

        print(f'\n{list}')

    elif option == 3:

        el = int(input('\nDigite o elemento a ser inserido: '))
        index = int(input('\nDigite o indice do novo elemento: '))

        list.insert(index, el)

        print(f'\n{list}')

    elif option == 4:

        if len(list) > 0:

            list.remove(list[0])

            if len(list) == 0:
                print('\nA lista esta vazia!')

            else:
                print(f'\n{list}')

        else:
            print('\nA lista esta vazia!')

    elif option == 5:

        if len(list) > 0:
            # list.pop()
            list.remove(list[len(list)-1])

            if len(list) == 0:
                print('\nA lista esta vazia!')

            else:
                print(f'\n{list}')

        else:
            print('\nA lista esta vazia!')

    elif option == 6:

        if len(list) > 0:

            el = int(input('\nDigite o elemento a ser removido: '))
            list.remove(el)

            if len(list) == 0:
                print('\nA lista esta vazia!')

            else:
                print(f'\n{list}')

        else:
            print('\nA lista esta vazia!')

    elif option == 7:

        if len(list) == 0:
            print('\nA lista esta vazia!\n')

        else:
            print(f'\nQuantidade de elementos na lista: {len(list)}')

    elif option == 8:

        index = int(input("\nDigite o indice: "))
        el = list[index]

        print(f'\nElemento na posicao {index}: {el}')

    elif option == 9:

        el = int(input("\nDigite o elemento: "))
        index = list.index(el)

        print(f'\nElemento na posicao {index}: {el}')

    elif option == 10:

        index = int(input("\nDigite o indice do elemento a ser alterado: "))
        el = int(input("Digite o novo elemento: "))

        list[index] = el

        if list[index] == el:
            print('\nAlteracao realizada com sucesso!\n')
            print(f'{list}')

        else:
            print('\nHouve um erro na alteracao!')

    elif option == 11:

        if len(list) == 0:
            print('\nA lista esta vazia!')

        else:
            print(f'\n{list}')

    elif option == 12:

        list.clear()

        if len(list) == 0:
            print('\nA lista esta vazia!')

    else:
        print("\nOpcao Invalida!")