# Customization Color and style
HEADER = '\033[95m'; OKBLUE = '\033[94m'; OKCYAN = '\033[96m'; OKGREEN = '\033[92m'; WARNING = '\033[93m'; FAIL = '\033[91m'; ENDC = '\033[0m'; BOLD = '\033[1m'; UNDERLINE = '\033[4m'
def printListItem(listItem):
    print(f'{HEADER}Your Item list: ')
    for i in range(len(listItem)):
        print(f'{OKBLUE}', (i + 1), f'.{OKCYAN}', listItem[i])

customList = []
isContinue = True
attemptCount = 0
while isContinue:
    print(f'{OKBLUE}{HEADER}{UNDERLINE} Menu list: {ENDC}\n'
          f'{OKCYAN}{BOLD} 1.{OKGREEN} Add Data {ENDC}\n'
          f'{OKCYAN}{BOLD} 2.{OKGREEN} Display Data {ENDC}\n'
          f'{OKCYAN}{BOLD} 3.{OKGREEN} Search Data {ENDC}\n'
          f'{OKCYAN}{BOLD} 4.{OKGREEN} Edit Data {ENDC}\n'
          f'{OKCYAN}{BOLD} 5.{FAIL} Delete Data {ENDC}\n'
          f'{OKCYAN}{BOLD} 6.{OKBLUE} Exit {ENDC}\n')
    inputText = input(f"{OKCYAN}Enter Your Choice : ")

    if inputText.strip() == '6':
        isContinue = False
        print(f'{HEADER}Good Bye !')

    elif inputText not in ['1','2','3','4','5','6']:
        attemptCount += 1
        if attemptCount >= 3:
            isContinue = False
            print(f'{FAIL} You Choose Wrong Input ! You Attempted{OKCYAN}', attemptCount, f'{FAIL}times\n'
                   f' Please Try Again. {WARNING}Your Wrong attempt exceed maximum time.')
        else:
            print(f'{FAIL} You Choose Wrong Input ! You Attempted{OKCYAN}', attemptCount, f'{FAIL}times\n'
                  f' Please Try Again.')

    elif inputText.strip() == '1' or len(customList) == 0:
        isAddList = True; isAddCompleted = False
        if len(customList) == 0:
            print(f'{WARNING} Your List is Empty, Please Add value first !')
        while  isAddList:
            if isAddCompleted:
                print(f'{HEADER} Do You want to Add more value in the List? {OKCYAN} "y/n"')
                confirmText = input('Confirm :').strip()
                if confirmText.lower() == 'n':
                    isAddList = False
                elif confirmText.lower() not in ['y','n']:
                    print(f'{WARNING}Please Type Correct input ! "y" or "n" ')
            if isAddList == True:
                print(f'{OKGREEN}Enter Value for Add to the list :\n'
                      f'You can add multiple value by adding comma {OKBLUE}","{OKGREEN} after value')
                inputValue = input('Value : ')
                if inputValue.__contains__(','):
                    splitedValue = inputValue.split(',')
                    if len(customList) == 0 and len(splitedValue) > 1:
                        for item in splitedValue:
                            customList.append(item)
                        isAddCompleted = True
                        printListItem(customList)
                    else:
                        customList.extend(splitedValue)
                        isAddCompleted = True
                        printListItem(customList)
                else:
                    customList.append(inputValue)
                    isAddCompleted = True
                    printListItem(customList)

    elif inputText.strip() == '2':
        isCompleted = False
        print(f'{HEADER}Your Item list: ')
        for i in range(len(customList)):
            print(f'{OKBLUE}',(i + 1),f'.{OKCYAN}', customList[i])
        print(f'\n{OKGREEN} Back To the main Menu Type {HEADER}"y"')
        while isCompleted == False:
            inputValue = input('Confirm : ').strip()
            if inputValue.lower() == 'y':
                isCompleted = True
                continue
            else:
                print(f'{WARNING}Please type the correcdt Input!')

    elif inputText.strip() == '3':
        isSearchList = True; isSearchCompleted = False
        while isSearchList:
            if isSearchCompleted:
                print(f'{HEADER} Do You want to Search more Item in the List? {OKCYAN} "y/n"')
                confirmText = input('Confirm :').strip()
                if confirmText.lower() == 'n':
                    isSearchList = False
                elif confirmText.lower() not in ['y','n']:
                    print(f'{WARNING}Please Type Correct input ! "y" or "n" ')

            if isSearchList == True:
                print(f'{HEADER}Please type your search item below.')
                inputValue = input('Search Value: ').strip()
                if len(inputValue) > 0:
                    searchItem = [i for i, x in enumerate(customList) if x == inputValue]
                    if len(searchItem) > 0:
                        print(f'{OKBLUE}Your Search item found in the list!')
                        for i in searchItem:
                            print(f'{OKBLUE}', (i + 1), f'.{OKCYAN}', customList[i])
                        isSearchCompleted = True
                    else:
                        print(f'{FAIL}Sorry ! Your Search Item does not found in the list!')
                        isSearchCompleted = True
                else:
                    print(f'{WARNING} Please type correct input!')
                    isSearchCompleted = True

    elif inputText.strip() == '4':
        isEditList = True; isEditCompleted = False
        while isEditList:
            if isEditCompleted:
                print(f'{HEADER} Do You want to Edit more Item in the List? {OKCYAN} "y/n"')
                confirmText = input('Confirm :').strip()
                if confirmText.lower() == 'n':
                    isEditList = False
                elif confirmText.lower() not in ['y','n']:
                    print(f'{WARNING}Please Type Correct input ! "y" or "n" ')

            if isEditList == True:
                print(f'{HEADER}Your Item list: ')
                for i in range(len(customList)):
                    print(f'{OKBLUE}', (i + 1), f'.{OKCYAN}', customList[i])

                print(f'{HEADER}Please type your Edit item {WARNING}Serial NO.# {HEADER}for Edit.')
                inputValue = input('Edit Item Serial No: ').strip()
                if int(inputValue) > 0:
                    editItem = customList[int(inputValue) - 1]
                    if len(editItem) > 0:
                        print(f'{OKBLUE}Your Edit item found in the list! and item is :{HEADER}',editItem)
                        print(f'{OKGREEN}Please Type the new value for Edit this {HEADER}',editItem,f'{OKGREEN}Item')
                        inputText = input(f'{OKBLUE} New Value : ').strip()
                        if len(inputText) > 0:
                            customList[int(inputValue) - 1] = inputText
                            print(f'{OKCYAN}Your Value updated Successfully !')
                            printListItem(customList)
                            isEditCompleted = True
                        else:
                            print(f'{WARNING} Please type correct input!')
                            isEditCompleted = True
                    else:
                        print(f'{FAIL}Sorry ! Your Edit Item does not found in the list!')
                        isEditCompleted = True
                else:
                    print(f'{WARNING} Please type correct input!')
                    isEditCompleted = True

    elif inputText.strip() == '5':
        isDeleteList = True; isDeleteCompleted = False
        while isDeleteList:
            if isDeleteCompleted:
                print(f'{HEADER} Do You want to Delete more Item from the List? {OKCYAN} "y/n"')
                confirmText = input('Confirm :').strip()
                if confirmText.lower() == 'n':
                    isDeleteList = False
                elif confirmText.lower() not in ['y','n']:
                    print(f'{WARNING}Please Type Correct input ! "y" or "n" ')

            if isDeleteList == True:
                print(f'{HEADER}Your Item list: ')
                for i in range(len(customList)):
                    print(f'{OKBLUE}', (i + 1), f'.{OKCYAN}', customList[i])

                print(f'{HEADER}Please type your Delete item {WARNING}Serial NO.# {HEADER}for Delete.')
                inputValue = input('Delete Item Serial No: ').strip()
                if int(inputValue) > 0:
                    deleteItem = customList[int(inputValue) - 1]
                    if len(deleteItem) > 0:
                        print(f'{OKBLUE}Are you sure to delete :{HEADER}',deleteItem)
                        print(f'{HEADER} Do You want to Delete more Item from the List? {OKCYAN} "y/n"')

                        inputText = input(f'{HEADER} Type "y/n" : ').strip()
                        if inputText.lower() == 'y':
                            customList.remove(deleteItem)
                            print(f'{OKCYAN}Your item Deleted Successfully !')
                            printListItem(customList)
                            isDeleteCompleted = True
                    else:
                        print(f'{FAIL}Sorry ! Your Delete Item does not found in the list!')
                        isDeleteCompleted = True
                else:
                    print(f'{WARNING} Please type correct input!')
                    isDeleteCompleted = True




