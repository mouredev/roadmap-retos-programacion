class Todo:
  def __init__(self, title, description, done, user, daysLeft):
    self.title = title
    self.description = description
    self.done = done
    self.user = user
    self.daysLeft = daysLeft

  def toggleStatus(self):
    self.done = not self.done
  
  def printTodo(self):
    print(f"""
      Title: {self.title}
      Description: {self.description}
      Done: {self.done}
      User: {self.user}
      Days left: {self.daysLeft}
    """)
  
newTodo = Todo('Test', 'Just testing', False, 'Andres', 4)

newTodo.printTodo()

newTodo.toggleStatus()

newTodo.printTodo()


# DIFICULTAD EXTRA

class Pila:
  def __init__(self, data):
    self.data = data

  def checkData(self):
    print(self.data)

  def addElement(self, value):
    return self.data.append(value)
  
  def deleteElement(self):
    return self.data.pop()

newPila = Pila([1, 2, 3])

newPila.checkData()
newPila.addElement(4)
newPila.addElement(5)
newPila.addElement(6)
newPila.checkData()
newPila.deleteElement()
newPila.checkData()

class Cola:
  def __init__(self, data):
    self.data = data

  def checkData(self):
    print(self.data)

  def addElement(self, value):
    return self.data.append(value)
  
  def deleteElement(self):
    return self.data.pop(0)

newCola = Cola([1, 2, 3])

newCola.checkData()
newCola.addElement(4)
newCola.addElement(5)
newCola.addElement(6)
newCola.checkData()
newCola.deleteElement()
newCola.checkData()