#Stacks - LIFO (Last In First Out)
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

#Queue - FIFO (First In First Out)
queue = []

queue.append(6)
queue.append(7)
queue.append(8)
queue.append(9)

print(queue)

print(queue.pop(0))
print(queue.pop(0))

print(queue)

#Extra exercises
#First

def browsing_web():

    moves = []

    while True:
        action = input("Add a URL or interact using the following words: forward, back, exit.")

        if action == "forward":
            pass
        elif action == "back":
            if len(moves) > 0:
                moves.pop()
        elif action == "exit":
            print(f"Leaving the website")
            break
        else:
            moves.append(action)
        
        if len(action) > 0:
            print(f"You have navigated to: {moves[len(moves) - 1]}")
        else:
            print("You are on the home page.")

browsing_web()

#Second

def print_doc():

    Docs = []

    while True:

        action = input("Add a document or select print/exit: ")

        if action == "exit":
            break
        elif action == "print":
            print(f"Printing: {Docs(0)}")
        else:
            Docs.append(action)

    print(f"Print queue: {Docs}")

print_doc()