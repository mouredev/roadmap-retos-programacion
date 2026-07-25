import requests

def preguntar(nombre):
    url = f"\nhttps://api.github.com/users/{nombre}"
    print(url)
    pregunta = requests.get(url).json()
    return pregunta

while True:
    nombre = input ("\nDIME EL NOMBRE DE USUARIO GITHUB ? (SALIR) ").lower()
    if nombre == "salir":
        break
    try:
        pregunta = preguntar(nombre)
        
        name = pregunta.get("name")
        print(f"\nNombre: {name}")
        
        if name == None:
            print ("\nUSUARIO NO DISPONIBLE")
        else:
            email = pregunta.get("email")
            print(f"\nEmail: {email}") 

            location = pregunta.get("location")
            print(f"\nPaís: {location}") 

            estrellas = pregunta.get("public_gists")
            print(f"\nEstrellas: {estrellas}") 

            creacion = pregunta.get("created_at")
            print(f"\nCreación: {creacion}") 

            bio = pregunta.get("bio")
            print(f"\nBio: {bio}") 

    except:
        print ("EL USUARIO NO EXISTE O NO DISPONIBLE\n")