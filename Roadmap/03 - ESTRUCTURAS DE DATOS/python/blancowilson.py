# Estructura de datos
#Listas
my_list:list = []
my_second_list:list = []

for i in range(5):
    my_list.append(i+1)
    my_second_list.append(2**i)

print(my_list)
print(my_second_list)
my_list.extend(my_second_list)
my_list.remove(2)
print(my_list)
print(my_list.index(2))
my_list.sort()
print(my_list)
## recorrer listas
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

print("usando ZIP")
questions = ['name', 'quest', 'favorite color', 'other cuestion','No matter this']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))



# Compresion de listas
my_second_list = [x**2 for x in range(10)]
print(my_second_list)
my_vector = []
x,y=0,0
my_vector = [(x,y) for x in range(10) for y in range(10)]
print(my_vector)
print(my_vector[51])

## En reversa
print("for using reversed")
for i in reversed(range(1, 10, 2)):
    print(i)

# sort a lis usin sorted
basket = sorted(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
for i in basket:
    print(i)
# El uso de set() en una secuencia elimina los elementos duplicados. El uso de sorted() en
# combinación con set() sobre una secuencia es una forma idiomática de recorrer elementos 
# únicos de la secuencia ordenada.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

print()
print("***** Diccionarios *******")

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
del tel['sape']
tel['irv'] = 4127
print(tel)
print("convertir a lista ",list(tel))
print(f'Verificar si un valor existe en diccionario "guido" in tel ,{"guido" in tel}')
## dos formas de crear un diccionario con dict
dictionari2=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
dictionari3=dict(sape=4139, guido=4127, jack=4098)
print(dictionari2)
print(dictionari3)
print(dictionari2 == dictionari3)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

from tkinter import *
from tkinter import ttk
contacts =[ {
    'name': 'John',
    'last_name': 'Doe',
    'phone': '123-456-7890',
    'email': 'john.doe@example.com'
}]


root = Tk()
root.title("Agenda")

name = StringVar()
last_name = StringVar()
phone = StringVar()
mail = StringVar()

def empty_table():
    rows = trvContacts.get_children()
    for row in rows:
        trvContacts.delete(row)

def fill_table():
    empty_table()
    for index,row in enumerate(contacts):
        print(index)
        trvContacts.insert('', END,index,text=index,values=tuple(row.values()) )


def add_contact():
    new_contac ={'name': name.get(),
     'last_name': last_name.get(),
     'phone': phone.get()}
    contacts.append(new_contac)
    fill_table()
   


def delte_contact():
    pass


def modify_contact():
    pass


frame = LabelFrame(root, text="Formualari de contacto")
frame.place(x=50, y=50, width=600, height=800)

lblname = Label(frame, text='Nombre').grid(column=0,row=0,padx=5,pady=10)
txtName = Entry(frame, textvariable=name)
txtName.grid(column=1, row=0,padx=5,pady=10)

lbllast_name = Label(frame, text='Apellido').grid(column=2,row=0,padx=5,pady=10)
txtlast_name = Entry(frame, textvariable=last_name)
txtlast_name.grid(column=3, row=0,padx=5,pady=10)

lblphone = Label(frame, text='Phone').grid(column=0,row=1)
txtphone = Entry(frame, textvariable=phone)
txtphone.grid(column=1, row=1)

lblmail = Label(frame, text='e-Mail').grid(column=2,row=1)
txtmail = Entry(frame, textvariable=mail)
txtmail.grid(column=3, row=1)

trvContacts = ttk.Treeview(frame)
trvContacts.grid(column=0,row=3,columnspan=4)
trvContacts["columns"]=('name','lastName','phone','mail')
trvContacts.column('#0',width=0,stretch=NO)
trvContacts.column('name',width=100,anchor=CENTER)
trvContacts.column('lastName',width=100,anchor=CENTER)
trvContacts.column('phone',width=50,anchor=CENTER)
trvContacts.column('mail',width=100,anchor=CENTER)
trvContacts.heading('#0', text='')
trvContacts.heading('name',text='Nombre',anchor=CENTER)
trvContacts.heading('lastName',text='Apellido',anchor=CENTER)
trvContacts.heading('phone',text='phone',anchor=CENTER)
trvContacts.heading('mail',text='e-Mail',anchor=CENTER)

btnDelete = Button(frame, text='Eliminar', command=lambda:delte_contact)
btnDelete.grid(column=1, row=4)
btnAdd = Button(frame, text='Agregar', command=add_contact)
btnAdd.grid(column=2, row=4)
btnModify = Button(frame, text='Eliminar', command=lambda:modify_contact)
btnModify.grid(column=3, row=4)






fill_table()

root.mainloop()


