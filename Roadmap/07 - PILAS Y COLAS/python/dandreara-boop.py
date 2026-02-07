

def pila ():
        print('+' * 30 , 'pila' , '+'*30)
        stack=[]
        stack.append(1)
        stack.append(2)
        stack.append(3)
        print (f'lista completa {stack}')
        print(f'eliminando ultimo en entrar {stack[(len(stack)-1)]}')
        del stack[(len(stack)-1)]
        print (f'lista actual elemento eliminado sin usar pop {stack}' )


        print (f'eliminando elemento por metodo pop {stack.pop()}')
        print (f'lista final {stack}')

def cola():
        print('+' * 30 , 'cola' , '+'*30)
        stack=[]
        stack.append(1)
        stack.append(2)
        stack.append(3)

        print (f'lista completa {stack}')
        print(f'primero en entrar {stack[0]}')
        del stack[0]
        print ('ultimo elemento eliminado sin usar pop' )


        print (f'eliminando por metodo pop {stack.pop(0)}')
        print (f'lista final {stack}')




def N_web():

        h_nav=[]
        posicion = -1

        while True:
                
                peticion=input("ingrese (p)proximo , (a) anterior , ingrese una nueva url (s)salir : ")
        
        

                if peticion == "a":
                        
                        
                        if posicion > 0 :
                                posicion -= 1
                                print (h_nav[posicion])
                        elif posicion == 0 :
                        
                                        print(f'estas en el comienzo {h_nav[posicion]}')
                        else :
                                print ('esta vacia')
                        

                        
                elif peticion == "p":
                        if posicion <0 :
                                print ('esta vacia')

                        elif posicion < (len(h_nav)-1):
                                posicion += 1
                                print(h_nav[posicion])

                        else :
                                print (f'estas en el fina {h_nav[posicion]}')
                
                elif peticion == "s":
                        break
                
                else :
                        h_nav.append(peticion)        
                        posicion=len(h_nav)-1
                        

def imprimir():
        cola=[]

        while True :
                peticion=input('ingrese documento ,s/salir,i/imprimir : ')
                
                if peticion == 's' :
                        break
                elif peticion == 'i':
                        if len(cola) > 0 :
                                print(cola.pop(0))
                else:
                        cola.append(peticion)


pila()
cola()
print ('+'*25, 'dificultad extra','+' *25)

while True:
        print('''
              1- Ejercicio navegador
              2- Ejercicio imprimir
              3- Salir ''')
        entrada=int(input('ingrese la opcion : '))
        if entrada==3:
                break
        elif entrada== 1:
                N_web()
        elif entrada==2:
                imprimir()


    
    