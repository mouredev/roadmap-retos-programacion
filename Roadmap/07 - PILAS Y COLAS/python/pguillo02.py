class Queue():
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)
    
    def __str__(self): 
        return str(self.queue)

