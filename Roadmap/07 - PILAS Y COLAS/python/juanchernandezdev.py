### Python Stracks And Queues ###

#! Stack

my_stack = []
print(my_stack)

my_stack.append(55)
my_stack.append(15)
my_stack.append(30)
my_stack.append(18)
print(my_stack)
my_stack.pop(-1)

print(my_stack)
  
#! Queue

my_queue = []
print(my_queue)

my_queue.append(120)
my_queue.append(15)
my_queue.append(88)
my_queue.append(4)
print(my_queue)
my_queue.pop(0)

print(my_queue)

#! Optional Challenge

my_stack = []

def navigation():
  while True:
    direction = input(f'Please enter an URL, "next", "before" to navigate or "exit" to stop the program: ').lower()
    
    if direction == 'exit':
      print('Exiting program')
      break
    elif direction == 'next':
      pass
    elif direction =='before':
      my_stack.pop()
    else:
      my_stack.append(direction)
      
    print(my_stack[len(my_stack) - 1])
      
navigation()

print_queue = []

def printer():
  while True:
    info = input(f'Please enter a document name, "print" to print a document, or "exit" to quit the program: ').lower()
    
    if info == 'exit':
      print('Exiting printer program.')
      break
    elif info == 'print':
      if len(print_queue) > 0:
        print(f'printing {print_queue.pop(0)}...')
      else:
        print('Print queue is empty')
    else:
      print_queue.append(info)
      
    print(f'Documents in queue {print_queue}')
    
printer()
    
