#FUNCIONES DEFINIDAS POR EL USUARIO

#Sin parámetros ni retorno
def Hola_mundo():
    print(f"Hola Mundo");

Hola_mundo();

#Con un parámetro
def Hola_usuario(usuario):
    print(f"Hola {usuario}");

Hola_usuario("User");

#Con varios parámetros
def Hola_usuarios(user1,user2):
    print(f"Hola {user1}, {user2}");

Hola_usuarios("User1", "User 2");

#Con retorno
def suma():
    return 2+3;
suma=suma();
print(suma);

#Con varios retornos
def nombre_y_edad():
    return "nombre", "edad";

nombre, edad = nombre_y_edad();
print(f"{nombre},{edad}");

#Con parametros variables
def nombre(*nombre):
    for n in nombre:
        print(f"{n}");

nombre("Nombre1", "Nombre2");




#Con parámetros variables y clave
def nombre_claves(**names):
    for key,value in names.items():
        print(f"{value}, {key}");

nombre_claves(language="Python");

#Funciones anidadas
def funcion_anidada():
    def funcion_de_dentro():
        print(f"Me he quedado sin frases absurdas para poner aqui");
    funcion_de_dentro();

funcion_anidada();


#FUNCIONES PROPIAS DEL LENGUAJE
frase = "Y ahora que pongo";
print(f"{frase}");
print(type(frase));
print(frase.split());



#VARIABLE GLOBALES Y LOCALES
variable_global = "A la variable global se accede desde cualquier parte del código";

def que_me_invento_ahora():
    variable_local = "A la variable local solo se accede desde dentro del bloque de la función definida";
    print(f"{variable_global}, {variable_local}")

que_me_invento_ahora();

print(f"{variable_global}");


#EXTRA
def numeros(Texto1,Texto2) -> int:
    counter = 0;
    for i in range(1,100+1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{Texto1},{Texto2}");
        elif i % 3 == 0:
            print(f"{Texto1}");
        elif i % 5 == 0:
            print(f"{Texto2}");
        else:
            print(i);
            counter += 1;
    return counter;


print(numeros("Texto1","Texto2"));