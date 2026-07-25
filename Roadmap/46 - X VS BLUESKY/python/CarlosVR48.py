"""
EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 *
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 *
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.  
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post,
 * fecha de creación y número total de likes.
 *
 * Controla errores en duplicados o acciones no permitidas.
"""
from pytz import timezone
from os import system
import datetime

def mostrar_posts(nombre):
    try:
        with open("post.txt", "x", encoding = "utf-8") as a:
            a.write("")
        with open("likes.txt", "x", encoding = "utf-8") as a:
            a.write("")
    except:
        pass
    #En la variable nombre esta puesto el nombre de usuario logeado
    usuario=nombre
    index = 1
    no_muestra = list()
    #Con la variable index se hace el recorrido 3 veces que son los datos del post
    #y se mira si el usuario logeado no sigue el post. se guarda el nombre del post
    #en la variable nombre
    with open(nombre, "r", encoding = "utf-8") as posts:
        for post in posts:
            if index == 2:
                nombre_desc = post
            elif index == 3:
                if post == "N\n":
                    no_muestra.append(nombre_desc)
                index = 0
            index = index + 1
             
    opcion = input("QUIERES CONTINUAR DONDE LO DEJASTES ? (S/N) ").upper()

    if opcion == "N":
        #Ahora se hace un recorrido por cada post
        contador = 1
        with open("post.txt", "r", encoding = "utf-8") as posts:
            for post in posts:
                if contador == 1:
                    numero_post = post
                elif contador == 2:
                    fecha = post
                elif contador == 3:
                    nombre = post    
                elif contador == 4:
                    contador = 0
                    links_total = 0
                    index = 1
                    # Se cuentan los likes que tiene el post
                    with open("likes.txt", "r", encoding = "utf-8") as likes:    
                        for like in likes:
                            if index == 1:
                                if numero_post == like: 
                                    links_total = links_total + 1
                            elif index == 3:
                                index = 0
                            
                            index = index + 1
                    
                    # Se comprueba el post y si esta en no_muestra no se enseña
                    if no_muestra.count(nombre) == 0 :
                        system("cls")
                        print ("-------------------------------------- RED SOCIAL XBLUE ---------------------------------------------\n")
                        print (f"{fecha}\n{nombre}\n{post}\nLIKES: {links_total}")
                        print ("-----------------------------------------------------------------------------------------------------\n")
                        sub_menu(nombre,numero_post,usuario)
                
                contador = contador + 1
    
    elif opcion == "S":
        try:    
            n=0
            #se lee el archivo continuar.txt si el nombre del usuario esta en el archivo se captura donde lo dejo
            index = 1
            with open("continua.txt", "r", encoding = "utf-8") as con:
                for c in con:
                    if index == 1:
                        u = c
                    elif index == 2:
                        index = 0
                        if f"{nombre}\n" == u:
                            n = c
                    index = index + 1
        except:
            pass
        
        contador = 1
        with open("post.txt", "r", encoding = "utf-8") as posts:
            for post in posts:
                if contador == 1:
                    numero_post = post
                elif contador == 2:
                    fecha = post
                elif contador == 3:
                    nombre = post    
                elif contador == 4:
                    contador = 0
                    # Se cuentan los likes que tiene el post
                    links_total = 0
                    index = 1
                    with open("likes.txt", "r", encoding = "utf-8") as likes:    
                        for like in likes:
                            if index == 1:
                                if numero_post == like: 
                                    links_total = links_total + 1
                            elif index == 3:
                                index = 0
                            
                            index = index + 1
                
                    if no_muestra.count(nombre) == 0 and int(n) <= int(numero_post):
                        system("cls")
                        print ("-------------------------------------- RED SOCIAL XBLUE ---------------------------------------------\n")
                        print (f"{fecha}\n{nombre}\n{post}\nLIKES: {links_total}")
                        print ("-----------------------------------------------------------------------------------------------------\n")
                        sub_menu(nombre,numero_post,usuario) 
                contador = contador + 1

#En este submenu se muestra la barra de navegacion y se escribe el resultado en el fichero del usuario logueado,
# para controlar los datos principales de la red social
 
def sub_menu(nombre,numero_post,usuario):
    index = 1
    opcion = input ("\n(L)IKE (D)ISLIKE (N)OSEGUIR (G)RABAR (ENTER CONTINUA) ").upper()
    
    if opcion == "G":
        try:
            with open("continua.txt", "a", encoding = "utf-8") as con:
                con.write(f"{usuario}\n")
                con.write(f"{numero_post}")
        except:
            with open("continua.txt", "w", encoding = "utf-8") as con:
                con.write(f"{usuario}\n")
                con.write(f"{numero_post}")

    if opcion == "L":
        like = False
        with open("likes.txt", "r", encoding = "utf-8") as posts:
            for post in posts:
                if index == 1 :
                    id_post = post
                elif index == 3 :
                    nom = post
                    index = 0
                    if id_post == numero_post and nom == f"{usuario}\n" :
                        like = True
                        input ("                 YA LE HAS DADO LIKE")
                index = index +1    
        
        if like == False:   
            with open("likes.txt", "a", encoding = "utf-8") as likes:
                likes.write(numero_post)
                likes.write(f"{nombre}")
                likes.write(f"{usuario}\n")
        
            with open(usuario, "a", encoding = "utf-8") as us:
                us.write(f"{numero_post}")
                us.write(f"{nombre}")
                us.write(f"{opcion}\n")

    if opcion =="D":
        #copio archivo likes en disklikes excepto el post que se ha hecho el dislike
        with open ("likes.txt", "r", encoding = "utf-8") as likes:
            with open ("dislike.bak", "w", encoding = "utf-8") as disbak:
                index = 1
                for like in likes:
                    if index == 1 :
                        nume = like
                    elif index == 2:
                        no = like
                    elif index == 3:
                        index = 0
                        use = like
                        if  nume == numero_post and use == f"{usuario}\n":
                            pass
                        else :
                            disbak.write(nume)
                            disbak.write(no)
                            disbak.write(use)
                    index = index + 1
        #ahora copio el archivo dislike a like 
        with open ("dislike.bak", "r", encoding = "utf-8") as dislikes:
            with open ("likes.txt", "w", encoding = "utf-8") as likes:
                index = 1
                for dislike in dislikes:
                    if index == 1 :
                        nume = dislike
                    elif index == 2:
                        no = dislike
                    elif index == 3:
                        use = dislike
                        likes.write(nume)
                        likes.write(no)
                        likes.write(use)
                        index = 0
                    index = index + 1

    if opcion == "N":    
        with open(usuario, "a", encoding = "utf-8") as posts:
            posts.write(f"{numero_post}")
            posts.write(f"{nombre}")
            posts.write(f"{opcion}\n")

def registro():
    #si no esta creado el archivo da un error
    try:
        with open("usuarios.txt", "x", encoding = "utf-8") as a:
            a.write("")
    except:
        pass

    index  = 1
    salir = 1
    coinciden = 0
    while salir :
        nombre = input ("\nCREA TU NOMBRE DE USUARIO (ENTER PARA SALIR) ? ")
        if nombre == "":
            salir = 0
        else:    
            #compruebo el nombre en la lista de usuarios que has introducido 
            with open("usuarios.txt", "r", encoding = "utf-8") as usuarios:
                for user in usuarios:
                    if index == 1:
                        usuario_log = user
                        if usuario_log == f"{nombre}\n":
                            input ( "    TU USUARIO YA ESTA INSCRITO!!! ")
                            salir=0
                            coinciden = 1

                    elif index == 2:
                        index = 0
                    
                    index = index +1
                    
                if coinciden == 0:
                    pasword = input ("    CREA TU CONTRASEÑA ? ")
                    #escribo nombre y password en usuario.txt
                    with open("usuarios.txt", "a", encoding = "utf-8") as usuarios:
                        usuarios.write(f"{nombre}")
                        usuarios.write(f"\n{pasword}\n")
                    #creo el archivo con el nombre de usuario para guardar datos
                    with open(nombre, "w", encoding = "utf-8") as nom:
                        nom.write("")
                    
                    input ("\nMUY BIEN YA PUEDES UTILIZAR LA RED SOCIAL!!! ")
                    return nombre

def id():
    marcador = 1
    nombre = input ("\n    DIME TU NOMBRE ? ")
    pasword = input ("    DIME TU CONTRASEÑA ? ")

    while True:
        #si el usuario quiere identificarse sin estar creado archivo usuarios da otro error
        try:
            #compruebo si existe el usuario
            with open("usuarios.txt", "r", encoding = "utf-8") as usuarios:
                    for user in usuarios:
                        if marcador == 1:
                            nombre_fichero = user
                        elif marcador == 2:
                            pasword_fichero = user
                            marcador = 0
                            if f"{nombre}\n" == nombre_fichero:
                                if f"{pasword}\n" == pasword_fichero:
                                    print (f"USUARIO: {nombre} ")
                                    return nombre,pasword
                                else:
                                    input ("CONTRASEÑA INVALIDA !!! ")
                                    return None,None
                        marcador = marcador + 1 
        except:
            input("    NO HAY USUARIOS INSCRITOS ")
            return None,None
           
        input("    TU USUARIO NO EXISTE !!! ")
        return None,None

def crear_post(nombre):
    salir = True
    fecha_hora = datetime.datetime.now(timezone("UTC"))
    fyh = datetime.datetime.strftime(fecha_hora,"%d-%m-%Y %H:%M:%S %z")
    numero_id = 0
    contador = 1
    try:
        with open("post.txt", "r", encoding = "utf-8") as posts:
            for post in posts:
                if contador == 1:
                    numero_id = post
                elif contador == 4:
                    contador = 0
                contador = contador + 1            
    except:
        pass

    numero_id = int(numero_id) + 1
    
    while salir:
            print ("\nEL POST NO DEVE SUPERAR LOS 200 CARACTERES. INTRODUCE EL POST...\n")
            post = input ()
            if len(post)>200:
                print ("    EL POST SUPERA LOS 200 CARACTERES !!!")
            else:
                salir = False

    with open("post.txt", "a", encoding = "utf-8") as pag:
        pag.write(f"{numero_id}\n")
        pag.write(f"{fyh}\n")
        pag.write(f"{nombre}\n")
        pag.write(f"{post}\n")

def elimina(nombre_log):
    contador = 1
    with open("post.txt", "r", encoding = "utf-8") as posts:
        with open("post.bak", "w", encoding = "utf-8") as bak:
            for post in posts:
                if contador == 1:
                    numero_post = post
                elif contador == 2:
                    fecha = post
                elif contador == 3:
                    nombre = post    
                elif contador == 4:
                    contador = 0
                    system("cls")
                    print ("-------------------------------------- RED SOCIAL XBLUE ---------------------------------------------\n")
                    print (f"{fecha}\n{nombre}\n{post}\n")
                    print ("-----------------------------------------------------------------------------------------------------\n")
                    
                    if nombre == f"{nombre_log}\n":
                        borrar = input  ("    QUERES BORRARLO (S/N) ? ").upper()
                        if borrar == "S":
                            pass
                        else:
                            bak.write(numero_post)
                            bak.write(fecha)
                            bak.write(nombre)
                            bak.write(post)
                    else:
                        bak.write(numero_post)
                        bak.write(fecha)
                        bak.write(nombre)
                        bak.write(post)
                contador = contador + 1
    
    with open("post.bak", "r", encoding = "utf-8") as bak:
        with open("post.txt", "w", encoding = "utf-8") as posts:
            for b in bak:
                posts.write(b)

def vfeed(usuario):
    index = 1
    with open("post.txt", "r", encoding = "utf-8") as posts:
        for post in posts:
            if index == 1 :
               id = post
            elif index == 2:
               fecha = post
            elif index == 3 :
                nombre = post
            elif index == 4 :
                index = 0
                text = post
                
                links_total = 0
                ind = 1
                with open("likes.txt", "r", encoding = "utf-8") as likes:    
                    for like in likes:
                        if ind == 1:
                            if id == like: 
                                links_total = links_total + 1
                        elif ind == 3:
                            ind = 0
                        ind = ind + 1

                if nombre == f"{usuario}\n" :
                    print ("-------------------------------------- RED SOCIAL XBLUE ---------------------------------------------\n")
                    print (f"{fecha}\n{nombre}\n{text}\nLIKES: {links_total}")
                    print ("-----------------------------------------------------------------------------------------------------\n")
                    
            index = index + 1
    
    input("    PULSA ENTER PARA CONTINUAR")

def vfeed_usuarios():
    usuario = input ("    DIME EL NOMBRE DEL USUARIO ? ")
    index = 1
    no_muestra = list()

    with open(usuario, "r", encoding = "utf-8") as posts:
        for post in posts:
            if index == 2:
                nombre_desc = post
            elif index == 3:
                if post == "N\n":
                    no_muestra.append(nombre_desc)
                index = 0
            index = index + 1
    
    index = 1
    with open("post.txt", "r", encoding = "utf-8") as posts:
        for post in posts:
            if index == 1 :
               id = post
            elif index == 2 :
               fecha = post
            elif index == 3 :
                nombre = post
            elif index == 4 :
                index = 0
                text = post
                
                ind = 1
                links_total = 0

                with open("likes.txt", "r", encoding = "utf-8") as likes:    
                    for like in likes:
                        if ind == 1:
                            if id == like: 
                                links_total = links_total + 1
                        elif ind == 3:
                            ind = 0
                        ind = ind + 1
                
                if no_muestra.count(nombre) == 0 and nombre != f"{usuario}\n":
                    print ("-------------------------------------- RED SOCIAL XBLUE ---------------------------------------------\n")
                    print (f"{fecha}\n{nombre}\n{text}\nLIKES: {links_total}")
                    print ("-----------------------------------------------------------------------------------------------------\n")

            index = index + 1
    
    input("    PULSA ENTER PARA CONTINUAR")

def menu_principal(nombre):
    salir = True
    while salir:
        hora_or = datetime.datetime.today()
        hora_utc = datetime.datetime.now(timezone("UTC"))
        hora_or_mod = datetime.datetime.strftime(hora_or,"%d-%m-%Y %H:%M:%S LOCAL")
        hora_utc_mod = datetime.datetime.strftime(hora_utc,"%d-%m-%Y %H:%M:%S UTC")
        system("cls")
        print (f"{hora_utc_mod}\n{hora_or_mod}\n\n--- RED SOCIAL XBLUE ---\n")
        print (f"    USUARIO: {nombre}\n")
        print ("    1 - REGISTRATE\n    2 - IDENTIFICATE\n    3 - CREAR POST\n    4 - MOSTRAR POSTS\n    5 - ELIMINA TUS POST\n    6 - V. FEED DEL USUARIO\n    7 - V. FEED DE LOS USUARIOS\n    8 - SALIR\n")
        seleccion = input("    QUE DESEAS HACER ? ")
        if seleccion == "1":
            nombre = registro()
        elif seleccion == "2":
            nombre, pasword = id()
        elif seleccion == "3" and nombre != None:
            crear_post(nombre)
        elif seleccion == "4" and nombre != None:
            mostrar_posts(nombre)
        elif seleccion == "5" and nombre != None:
            elimina(nombre)
        elif seleccion == "6" and nombre != None:
            vfeed(nombre)
        elif seleccion == "7" and nombre != None:
            vfeed_usuarios()
        elif seleccion == "8" :
            salir = False

nombre = None
menu_principal(nombre)

# Archivo (post.txt) guarda todos los post . Id post , fecha UTC de creacion , nombre del usuario y texto.
# Archivo (usuarios) guarda todo los usuarios y sus contraseñas.
# Archivo (nombreusuario) guarda todo el historial generado. Id del post , nombre al que le haces la accion y accion
# Archivo (likes.txt) guarda todo lo relacionado con like. Id del mensage , nombre associado al post y nombre del usuario
# Archivo (continua.txt) guarda el nombre del usuario y el numero donde lo has grabado