class myClass:
    public_attribute = "This is a public attribute"
    _private_attribute = 0
    def __init__(self):
        self._private_attribute = 1
        print("Class constructor")
    
    def print_attributes(self):
        print("Public attribute: ",self.public_attribute) 
        print("Private attribute: ", self._private_attribute) 
    
    def get_public_attribute(self):
        return self.public_attribute 
    def get_private_attribute(self):
        return self._private_attribute
    def set_private_attribute(self,value):
        self._private_attribute = value
    def set_public_attribute(self,value):
        self.public_attribute = value       
        
        
class_instance = myClass() #Constructor will be triggered
class_instance.print_attributes()
class_instance.set_public_attribute("Hello!")
class_instance.set_private_attribute(5)
print("Public attribute", class_instance.get_public_attribute())
print("Private attribute", class_instance.get_private_attribute())

#Extra exercise

class myQueue:
    
    def __init__(self):
        self.queue = []
    
    def push(self,element):
        self.queue.append(element)    
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)   
    def count(self)->int:
        return len(self.queue)
    def print_content(self):
        print("Content of the queue", self.queue)
            
        
my_queue_object = myQueue() 
my_queue_object.push(3)
my_queue_object.push("Hola")
my_queue_object.push("adios")
print("Number of elements: ", my_queue_object.count())
my_queue_object.print_content()
print(my_queue_object.pop()) 
print(my_queue_object.pop()) 
print(my_queue_object.pop()) 

class myStack():
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element) 
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
    def count(self)->int:
        return len(self.stack)
    def print_content(self):
        print("Content of the stack", self.stack)
            

my_stack_object = myStack()
my_stack_object.push(5)
my_stack_object.push(8)
print("Number of objects: ", my_stack_object.count())
my_stack_object.print_content()
print(my_stack_object.pop())               
print(my_stack_object.pop())
           