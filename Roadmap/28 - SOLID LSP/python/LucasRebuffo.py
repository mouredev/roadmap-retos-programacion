""" /*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */ """

""" Principio de Sustitucion de Liskov

    El principio de Liskov platea que si tenemos una clase A y una clase B que hereda de A
    Las instacias de A pueden ser reemplazadas por instacias de la clase B sin afectar a la
    integridad del programa
 """

""" Ejemplo forma incorrecta """


class Pajaro:

    def comer(self):
        return "comida"

    def cantar(self):
        return "canto"

    def volar(self):
        if type(self) == type(Avestruz()):
            raise Exception("El avestruz no puede volar")
        pass


class Aguila(Pajaro):

    def comer(self):
        return "pescado"

    def cantar(self):
        return "chillido"


class Avestruz(Pajaro):

    def comer(self):
        return "comida de avestruz?"

    def cantar(self):
        return "graznido"

    def volar(self):
        raise Exception("El avestruz no puede volar")


""" Aca vemos que con el Aguila no hay poblema ya que es intercambiable con Pajaro, pero
    con el avestruz no, ya que un aveztruz no puede volar. Lo intentamos corregir con la
    excepcion y agregando un chqeueo en la calse Pajaro pero ahi rompemos el pricipio 
    ya que la clases se tienen que conocer.  """

""" Ejemplo forma correcta """

""" Lo que podemos hacer para solucionar es agregar otra clase PajaroVolador y agreagr el metodo volar alli"""


class Pajaro:

    def comer(self):
        return "comida"

    def cantar(self):
        return "canto"


class PajaroVolador(Pajaro):
    def volar(self):
        # Logica para volar
        pass


class Aguila(PajaroVolador):

    def comer(self):
        return "pescado"

    def cantar(self):
        return "chillido"


class Avestruz(Pajaro):

    def comer(self):
        return "comida de avestruz?"

    def cantar(self):
        return "graznido"


""" Ahora no necesitamos las excepciones ya que las clases son intercambiables entre si """

""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */  """


class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass


class Bicicleta(Vehiculo):

    def acelerar(self):
        print("Pedaleando muy fuerte !!!")

    def frenar(self):
        print("Clavo los frenos !!!")


class Automovil(Vehiculo):

    def acelerar(self):
        print("Pisteando como un campeon ;)")

    def frenar(self):
        print("Uff casi te llevas puesto una viejita")


class Motocicleta(Vehiculo):

    def acelerar(self):
        print("Estas para el rally Dakar ")

    def frenar(self):
        print("Darrapas 5 metros y te frenas")


bici = Bicicleta()
moto = Motocicleta()
auto = Automovil()

bici.acelerar()
bici.frenar()

auto.acelerar()
auto.frenar()

moto.acelerar()
moto.frenar()
