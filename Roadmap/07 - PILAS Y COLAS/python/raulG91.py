#Stack


def stack_add_element(stack,element):
    stack.append(element)

def stack_remove_element(stack):
    
    return stack.pop()
        
        
stack = []
stack_add_element(stack,5)
stack_add_element(stack,23)
stack_add_element(stack,5)
print(stack)
print("Delete last element ",stack_remove_element(stack))
print(stack)      

#Queue
def queue_add_element(queue,element):
    
    queue.append(element)
    
def queue_remove_element(queue):
    
    if len(queue) > 0:
        return queue.pop(0)    
    
queue = []
queue_add_element(queue,8)   
queue_add_element(queue,6)
queue_add_element(queue,0)
print(queue)
print("Delete first element ", queue_remove_element(queue))
print(queue)

#Extra exercise

def browser():
    browser = []
    history = []
    current = ""
    index = 0
    while True:
        option = input("Introduzca adelante/atras o salir ")
        if option == "adelante":
            if(index +1)< len(browser):
                stack_add_element(history,current)

                index+=1
                current = browser[index]
                
            print("Pagina actual: ",current)
                
        elif option == "atras":
            if len(history)>0:
                current = stack_remove_element(history)
                index-=1
            print("Pagina actual: ",current)
            
                    
        elif option == "salir":
            break
        else:
            browser.append(option)
            if len(browser) > 1:
                stack_add_element(history,current)
            current = option
            if len(browser)> 1:
                index+=1
            print("Pagina actual: ",current)

     
            
browser()            
            
def printer():
    printer_queue = []
    
    while True:
        option = input("Introduzca documento, imprimir,  salir ")
        if option == "imprimir":
            print("Imprimendo: ",queue_remove_element(printer_queue))
        elif option == "salir":
            break
        else:
            queue_add_element(printer_queue,option)          
                       
printer()                        