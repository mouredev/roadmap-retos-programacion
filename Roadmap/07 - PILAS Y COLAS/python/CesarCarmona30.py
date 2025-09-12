class Stack:

  def __init__(self):
    self.data = []

  def push(self, element):
    self.data.append(element)

  def pop(self):
    try:
      element = self.data.pop()
    except IndexError as e:
      print(f'Error: {type(e).__name__}, empty stack')
      return
    print(f'Stack element out: {element}')

  def showData(self):
    print(f'Stack: {self.data}')

class Queue:

  def __init__(self):
    self.data = []

  def enqueue(self, element):
    self.data.append(element)

  def dequeue(self):
    try:
      element = self.data.pop(0)
    except IndexError as e:
      print(f'Error: {type(e).__name__}, empty queue')
      return
    print(f'Queue element out: {element}')

  def showData(self):
    print(f'Queue: {self.data}')

veggies = Stack()
veggies.push('Cucumber')
veggies.push('Radish')
veggies.push('Tomato')
veggies.push('Orange')
veggies.push('Apple')
veggies.showData()
veggies.pop()
veggies.pop()
veggies.showData()

fruits = Queue()
fruits.enqueue('Banana')
fruits.enqueue('Melon')
fruits.enqueue('Strawberry')
fruits.enqueue('Onion')
fruits.enqueue('Garlic')
fruits.showData()
fruits.dequeue()
fruits.dequeue()
fruits.showData()

class Browser(Stack):
  
  def __init__(self):
    super().__init__()
    self.currentPage = None
    self.index = None

  def addPage(self, page):
    self.push(page)
    self.index = len(self.data) - 1
    self.currentPage = self.data[self.index]

  def goBack(self):
    try:
      self.index -= 1
      self.currentPage = self.data[self.index]
      return self.currentPage
    except Exception:
      print('Sin páginas en el historial')
      return '-'

  def goForward(self):
    try:
      self.index += 1
      self.currentPage = self.data[self.index]
      return self.currentPage
    except Exception:
      print('Sin referencia de página adelante')
      return '-'

def history(browser):
  while True:
    option = input('>_')
    page = ''
    match option.lower():
      case 'adelante':
        page = browser.goForward()
        print(f'Página actual: {page}')
      case 'atras':
        page = browser.goBack()
        print(f'Página actual: {page}')
      case 'salir':
        break
      case _:
        new_page = option
        browser.addPage(new_page)
        print(f'Nueva página: {new_page}')

myBrowser = Browser()
history(myBrowser)

class Printer(Queue):
  def __init__(self):
    super().__init__()
  
  def printDoc(self):
    printout = self.dequeue()
    return printout

  def addDoc(self, doc):
    self.enqueue(doc)

  def dequeue(self):
    try:
      element = self.data.pop(0)
      return element
    except Exception:
      return 'No hay elemento'
    
def printQueue(printer):
  while True:
    option = input('doc name: ')
    match option.lower():
      case 'imprimir':
        docPrinted = printer.printDoc()
        print(f'Documento impreso: {docPrinted}')
      case 'salir':
        break
      case _:
        new_doc = option
        printer.addDoc(new_doc)

myPrinter = Printer()
printQueue(myPrinter)