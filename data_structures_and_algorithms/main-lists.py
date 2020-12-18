from lists.linked_list import LinkedList

list = LinkedList()

while True:
    print('Menu de opcoes:')
    print('1  - Inserir elemento inicio')
    print('2  - Inserir elemento final')
    print('3  - Inserir elemento (ordenado)')
    print('4  - Inserir elemento (qualquer posicao)')
    print('5  - Remover elemento inicio')
    print('6  - Remover elemento final')
    print('7  - Remover elemento (qualquer)')
    print('8  - Obter quantidade de elementos na lista')
    print('9  - Obter elemento pelo indice')
    print('10 - Obter indice pelo elemento')
    print('11 - Alterar elemento')
    print('12 - Impirmir lista')
    print('13 - Limpar lista')
    option = input('Opcao:')

    if option == 1:
        el = int(input('\nDigite o elemento a ser inserido: '))
        list.insert(el)

        print(f'\n{list}')

    elif option == 2:
       el = int(input('\nDigite o elemento a ser inserido: '))

       list.push(el)
       print(f'\n{list}')

    elif option == 3:

       el = int(input('\nDigite o elemento a ser inserido: '))
       list.sortedInsert(el)

       print(f'\n{list}')

    elif option == 4:

       el = int(input('\nDigite o elemento a ser inserido: '))
       index = int(input('\nDigite o indice do novo elemento: '))

       if list.insert(el, index) != None:
            print(f'\n{list}')
       else:
            print('\nFalha na insercao!')

    elif option == 5:

        if list.isEmpty() != None:
            list.removeAt(0)

            if list.isEmpty() != None:
                print('\nA lista esta vazia!')

            else:
                print(f'\n{list}')

        else:
            print('\nA lista esta vazia!')

    elif option == 6:

        if list.isEmpty() != None:
            list.pop()
            
            if list.isEmpty() != None:
                print('\nA lista esta vazia!')

            else:
                print(f'\n{list}')

        else:
            print('\nA lista esta vazia!')
        
    elif option == 7:

        if (!list.isEmpty()) {
            el = questionInt('\nDigite o elemento a ser removido: ')
            index = list.indexOf(el)

            if (index != = -1) {
                list.removeAt(index)

                if (list.isEmpty()) {
                    console.log('\nA lista esta vazia!')

                } else {
                    print(f'\n{list}')
                }

            } else {
                console.log('\nElemento nao encontrado!')
            }

        } else {
            console.log('\nA lista esta vazia!')

        }

    elif option == 8:

        if (list.isEmpty()) {
            console.log('\nA lista esta vazia!')

        } else {

            print('\nQuantidade de elementos na lista: ${list.length}`)
        }

    elif option == 9:
        
        index = questionInt("\nDigite o indice: ")
        el = list.getElementAt(index)

        if (el != = undefined) {
            print('\nElemento na posicao ${index}: ${el}`)

        } else {
            console.log('\nElemento nao encontrado!')
        }

elif option == 10:

        el = questionInt("\nDigite o elemento: ")
        index = list.indexOf(el)

        if (list.indexOf(el) != = -1) {
            print('\nElemento na posicao ${index}: ${el}`)

        } else {
            console.log('\nElemento nao encontrado!')
        }

elif option == 11

        index = questionInt("\nDigite o indice do elemento a ser alterado: ")
        el = questionInt("Digite o novo elemento: ")

        list.setElementAt(el, index)

        if (list.getElementAt(index) == = el) {
            print('\nAlteracao realizada com sucesso!\n`)
            console.log(list.toString())

        } else {
            print('\nHouve um erro na alteracao!`)
        }

elif option == 12:

        if (list.isEmpty()) {
            console.log('\nA lista esta vazia!');} else {
            print(f'\n{list}')

        }

elif option == 13: {

        list.clear()

        if (list.isEmpty() != None) {
            console.log('\nA lista esta vazia!')
        }

    } else {
        console.log("\nOpcao Invalida!")
    }

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
