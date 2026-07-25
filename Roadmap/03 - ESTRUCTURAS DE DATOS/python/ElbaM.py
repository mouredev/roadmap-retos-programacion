#### Estructuras de Datos
# Listas : crear, insertar, actualizar, eliminaer y ordenar Son Mutables
ls=[]
ln=list(range(1,11))
print(ln)
print(type(ln))
print (type(ls))
ls.append('a')
ls.append('c')
ls.append('d')
print(ls)
ls[1]='b'
print(ls)
ls.pop(2)
print(ls)
ls.append('c')
ls.append('m')
ls.append('k')
ls.append('e')
ls.append('r')
ls.append('p')
print(ls)
ls.sort()
print(ls)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)
del a[0]
print (a)


# tuplas: crear, insertar,  NO se pueden actualizar, NO se pueden eliminar y ordenar Son Inmutables
t1=()
t2=(1,2,3,4)    
t3 = (5, 6, 7)
t4=(10,20, 'hola')
x, y, z = t4
tunica='Uno',
print(type(t1), type(t2), type(t3), type(t4), type(tunica))
print (tunica)

# SET: crear, insertar, actualizar, eliminaer y NO se pueden ordenar Son Mutables aceptan solo datos unicos
conjun1= set()
conjun2={'elba', 'marina', 'mujica', 'romero', 'elba'}
conjun3= {'gustavo', 'luis', 'gaby'}
conjun4= set('abracadraba')    
print(type(conjun1), type(conjun2), type(conjun3), type(conjun4))
print (conjun1)
print(conjun2)
print(conjun3)
print(conjun4)
conjun4.remove ('a') 
print(conjun4)

#comprension
aba = {x for x in 'abracadabra' if x not in 'abc'}
print(aba)   


# DICCIONARIOS: crear, insertar, actualizar, eliminaer,  ordenar Son Mutables 

dicc1={}
dicc2={'nombre':'elba', 'edad': 55, 'cursos':['python', 'GENAI']}   
dicc3= dict(nombre='elba', apellido='Mujica', trabajos=['GEMTE', 'TECNosotros'])
print(type(dicc1), type(dicc2), type(dicc3))
print(dicc1)
print(dicc2)
print(dicc3)
del dicc2['edad']
print(dicc2)

#comprension
dicc5= {x: x**2 for x in (2, 4, 6)}
print(dicc5)

#Pruebas de concepto
#nombre=input('Ingrese su nombre Contacto ')
#telefono=input('Registre Nuevo Telefono ' )
#pruebas={nombre:telefono}
#print(pruebas)


# complejidad EXTRA

# 1. Crear un programa que permita ingresar el nombre, telefono  de una persona
# y guarde esos datos en una lista. El programa debe permitir ingresar los datos de

agenda={}
entrar=True

def valida_numero(telefonov):    
    if telefonov.isdigit() and len(telefonov)<=11:
        return True
    else:
        print('Telefono no valido. Intente de nuevo')
        return False

def incluir_contacto(agenda):
    nombre=input('Ingrese nombre Contacto: ')
    telefono=input('Registre Telefono Contacto: ')
    if valida_numero(telefono):
       print(nombre, telefono)
       agenda[nombre]= telefono   
      # print(agenda)
    return

def editar_contacto(agenda):
    nombreE=input('Ingrese nombre Contacto a Editar')
    telefonon=input('Registre Nuevo Telefono ' )
    if valida_numero(telefonon):
        agenda[nombreE]= telefonon   
      # print(agenda)
    return

def eliminar_contacto(agenda):
    nombre=input('Ingrese su nombre Contacto a Eliminar')
    del agenda[nombre]
    print(agenda)
    return

def buscar_contacto(agenda):
    nombreb=input('Ingrese su nombre Contacto a Buscar')
    print(agenda[nombreb])
    return

def menu():
    print ('AGENDA DE CONTACTO')
    print  ('iNGRESE opcion') 
    print ('1. Ingresar Contacto')
    print ('2. Editar Contacto')
    print ('3. Eliminar Contacto')
    print ('4. Buscar Contacto')
    print ('5. Listar Agenda')
    print ('6 Salir')
    return
 
def listar_agenda(agenda):
    for k, v in agenda.items():
        print(k, v)
    return


while entrar == True:
    menu()
    opcion=input('Ingrese Opcion: ')
    match opcion:
        case '1':
            incluir_contacto(agenda)
        case '2':
            editar_contacto (agenda)
        case '3':
            eliminar_contacto (agenda)
        case '4':
            buscar_contacto (agenda) 
        case '5':
            # for k, v in agenda.items():
            #     print(k, v)
            listar_agenda (agenda)
            #print(agenda)
        case '6':
            entrar=False
            print ('Hasta Luego')
            exit
        case _:
            print ('Opcion no valida')     









