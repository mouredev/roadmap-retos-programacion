# 
# EJERCICIO:
# Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
# números del 1 al 10 mediante iteración.
# 
# DIFICULTAD EXTRA (opcional):
# Escribe el mayor número de mecanismos que posea tu lenguaje
# para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
# 
email_listado = [
    "usuario123@gmail.com",
    "nombre.apellido@empresa.es",
    "info-ventas@dominio.net",
    "soporte@techsolutions.org",
    "contacto.oficial@servicio.com.mx",
    "j.perez_dev@agencia.io",
    "proyecto_alfa@mailinator.com",
    "laura.fernandez@universidad.edu",
    "admin@misitio.blog",
    "dev_testing_01@testserver.dev",
    "martin-gomez-45@yahoo.es",
    "recepcion@hotelparadise.com",
    "inversiones.2025@finance.co",
    "cliente-vip@premiumservices.us",
    "marta.sanz@publicaciones.cat",
    "notificaciones@appmovil.net",
    "registro_temporal@tempmail.org",
    "elena.rodriguez.s@otroservidor.net",
    "secretaria.ejecutiva@consorcio.es",
    "postmaster@localhost.localdomain" # Un email técnico
]

def serparacion(cadena) -> str:
    print('{}'.format(cadena * 20))

class MyIteratorNext:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

class MyIteratorExp:
    def __iter__(self):
        self.a = 2
        return self
    
    def __next__(self):
        x = self.a
        self.a *= 2
        return x

def day_of_week(): # Es un bucle infinito
    i = 0
    days= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while True:
        yield days[i % 7]
        i += 1

def colours():
    while True:
        yield "black"
        yield "yellow"
        yield "orange"
        yield "blue"

def main():
    for num in range(1,11):
        print(num)
    serparacion('-***-')

    numb = 1
    while numb <= 10:
        print(numb)
        numb += 1
    serparacion('-***-')

    print([n + 1 for n in range(10)])
    serparacion('-***-')

    for mail in email_listado:
        print(mail)
    serparacion('-***-')

    myiterator = MyIteratorNext()
    myiter = iter(myiterator)
    while myiter.a <= 10:
        print(myiter.a)
        next(myiter)
    serparacion('-***-')

    myiteratorexp = MyIteratorExp()
    myitere = iter(myiteratorexp)
    while myitere.a <= 1024:
        print(myitere.a)
        next(myitere)
    serparacion('-***-')

    counter = 0
    for x in day_of_week():
        if counter >= 7:
            break
        print(x)
        counter += 1
    serparacion('-***-')

    colour = colours()
    counter = 0
    for x in range(8):
        print(next(colour))
    serparacion('-***-')
        
main()
