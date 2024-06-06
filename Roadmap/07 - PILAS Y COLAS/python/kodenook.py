"""
    Stack
"""

letters = ['a', 'b', 'c', 'd']

''' insert '''

letters.append('e')
letters.append('f')

print(letters)

''' delete '''

letters.pop()

print(letters)

"""
    Queue
"""

letters = ['a', 'b', 'c', 'd']

''' insert '''

letters.append('e')
letters.append('f')

print(letters)

''' delete '''

del letters[0]

print(letters)

"""
    Exercise
"""

def web_navigation() -> None:

    stack = []
    option = ''

    while option != 'exit':

        option = input('give a url or next, before, exit: ')

        if option == 'next':
            pass
        elif option == 'before':
            stack.pop()
            print(f'you are in {stack[-1]}')
        else:
            stack.append(option)
            print(f'you are in {stack[-1]}')

web_navigation()

def shared_print() -> None:
    queue = []
    option = ''

    while option != 'exit':

        option = input( 'give a document or print, exit: ')

        if option == 'print':
            printed = queue[0]
            del queue[0]
            print(f'you printed {printed}')
        else:
            queue.append(option)


shared_print()