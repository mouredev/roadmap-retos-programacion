#stacks

stack = ["a", "b", "c"]
stack.append("d")
stack.append("e")
stack.pop()

print(stack)

#queues

queue = ["a", "b", "c"]
queue.append("d")
queue.append("e")
queue.pop(0)

print(queue)

#deque

from collections import deque

queue = deque(["a", "b", "c"])
queue.append("d")
queue.append("e")
queue.popleft()

print(queue)

'''
Extra
'''



#Stack

def back_and_forth():
    history = []
    ahead = []
    
    while True:
        command = input("Enter a website, 'back' to go back, 'forward' to go forward, or 'exit' to quit: ")

        if command == "exit":
            break
        elif command == "back":
            if len(history) > 1:
                ahead.append(history.pop())
                print("Current:", history[-1])
            else:
                print("No more history to go back to.")
        elif command == "forward":
            if ahead:
                history.append(ahead.pop())
                print("Current:", history[-1])
            else:
                print("No forward history available.")
        else:
            history.append(command)
            ahead.clear()
            print("Current:", command)

back_and_forth()

#Queue

def printer():
    print_queue = []
    
    while True:
        command = input("Enter a document name to add to the queue, 'print' to print, or 'exit' to quit: ")

        if command == "exit":
            break
        elif command == "print":
            if print_queue:
                print("Printing:", print_queue.pop(0))
            else:
                print("The queue is empty. No documents to print.")
        else:
            print_queue.append(command)
            print(f"'{command}' added to the queue.")

printer()
