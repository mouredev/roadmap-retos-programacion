# #07 PILAS Y COLAS

# Pilas/Stack (LIFO)

stack = []
stack.append("libro 1") # push
stack.append("libro 2") # push
stack.append("libro 3") # push

print(stack)

stack.pop()
print(stack) # pop

# Colas/Queue (FIFO)

queue = []
queue.append("cliente 1") # enqueue
queue.append("cliente 2") # enqueue
queue.append("cliente 3") # enqueue

print(queue)

queue.pop(0) # dequeue
print(queue)

# Extra

def browser():
    stack = []

    while True:
        option = input("Enter url or select Next / Previous / Exit: ").lower()

        match option:
            case "exit":
                print("Exiting...")
                break
            case "previous":
                if len(stack) > 0:
                    print(f"URL: {stack[-1]}")
                    stack.pop()
            case "next":
                pass
            case _:
                stack.append(option)


#browser()

def printer():
    queue = []

    while True:
        option = input("Enter document or select Print / Exit: ").lower()

        match option:
            case "exit":
                print("Exiting...")
                break
            case "print":
                if len(queue) > 0:
                    print(f"Printing: {queue[0]}")
                    queue.pop(0)
            case _:
                queue.append(option)
                print(f"Document added: {option}")


printer()