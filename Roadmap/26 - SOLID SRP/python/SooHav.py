# 26 SOLID: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
import logging
# Ejercicio
# Ejemplo Pato sin SRP


class Pato:

    def __init__(self, nombre):
        self.nombre = nombre

    def vuela(self):
        print(f"{self.nombre} vuela.")

    def nada(self):
        print(f"{self.nombre} nada.")

    def dice(self) -> str:
        return "Quack"

    def saluda(self, pato2):
        print(f"{self.nombre}: {self.dice()}, hola {pato2.nombre}")


# Uso
print("Sin SRP")
pato1 = Pato(nombre="Daisy")
pato2 = Pato(nombre="Donald")
pato1.vuela()
pato1.nada()
pato1.saluda(pato2)
print("\n")

# Ejemplo Pato con SRP


class Pato():
    """Clase que define los patos"""

    def __init__(self, nombre):
        self.nombre = nombre

    def vuela(self):
        print(f"{self.nombre} vuela.")

    def nada(self):
        print(f"{self.nombre} nada.")

    def dice(self) -> str:
        return "Quack"


class Dialogo():
    """Clase que define la comunicacion entre patos"""

    def __init__(self, formato):
        self.formato = formato

    def conversacion(self, pato1: Pato, pato2: Pato):
        frase1 = f"{pato1.nombre}: {pato1.dice()}, ¡Ay, {
            pato2.nombre}! ¡Casi me caigo al intentar atrapar un pez!"
        frase2 = f"{pato2.nombre}: {pato2.dice()}, ¡Otra vez, {
            pato1.nombre}? Ten más cuidado la próxima vez."
        conversacion = [frase1, frase2]
        print(*conversacion,
              f"(Extracto de {self.formato})",
              sep='\n')


# Uso
print("Con SRP")
pato1 = Pato(nombre="Donald")
pato2 = Pato(nombre="Daisy")
pato1.vuela()
pato2.nada()
formato1 = Dialogo(formato="historieta")
formato1.conversacion(pato1, pato2)

# Extra
# Programa sin SRP


class GestorBiblioteca():
    """
    Clase que gestiona una biblioteca.
    """

    def __init__(self):
        self.registro = {}
        self.usuarios = {}

    def registro_libros(self, id, titulo, autor, cantidad_copias, max_prestamo):
        """
        Funcion que registra un libro.
        """
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "cantidad_copias": cantidad_copias,
            "max_prestamo": max_prestamo
        }
        self.registro[id] = nuevo_libro
        print(f"Libro '{titulo}' agregado con éxito.")

    def agregar_usuario(self,  id, nombre, dni, email):
        """
        Funcion que permite agregar nuevos usuarios con información básica.
        """
        nuevo_usuario = {
            "nombre": nombre,
            "dni": dni,
            "email": email
        }
        self.usuarios[id] = nuevo_usuario
        print(f"Usuario '{nombre}' agregado con éxito.")

    def prestamo_libro(self, titulo, nombre):
        """
        Funcion para que los usuarios puedan tomar prestados libros.
        """
        usuario_registrado = False
        for usuario in self.usuarios.values():
            if usuario["nombre"] == nombre:
                usuario_registrado = True
                break

        if not usuario_registrado:
            print(f"Usuario '{
                  nombre}' no está registrado. No puede tomar prestado libros para llevar a casa.")
            return

        libro_prestado = None
        cantidad_actual = None

        for id, nuevo_registro in self.registro.items():
            if nuevo_registro["titulo"] == titulo:
                libro_prestado = nuevo_registro
                cantidad_actual = nuevo_registro["cantidad_copias"]
                max_prestamo = nuevo_registro["max_prestamo"]
                break

        if libro_prestado:
            if cantidad_actual > 0 and cantidad_actual <= max_prestamo:
                cantidad_actual -= 1
                libro_prestado["cantidad_copias"] = cantidad_actual
                print(f"Libro '{titulo}' prestado con éxito a {nombre}.")
            else:
                print(f"Libro '{
                      titulo}' no tiene copias disponibles o se ha excedido el máximo préstamo.")
        else:
            print(f"Libro '{titulo}' sin existencias.")

    def devolucion_libro(self, titulo, nombre):
        """
        Funcion para que los usuarios puedan devolver libros.
        """
        usuario_registrado = False
        for usuario in self.usuarios.values():
            if usuario["nombre"] == nombre:
                usuario_registrado = True
                break

        if not usuario_registrado:
            print(f"Usuario '{
                  nombre}' no está registrado. Pida el nombre o id de la persona que tomo prestado el libro.")
            return

        libro_devuelto = None

        for id, nuevo_registro in self.registro.items():
            if nuevo_registro["titulo"] == titulo:
                libro_devuelto = nuevo_registro
                cantidad_actual = nuevo_registro["cantidad_copias"]
                max_prestamo = nuevo_registro["max_prestamo"]
                break

        if libro_devuelto:
            cantidad_actual_nueva = cantidad_actual + 1
            if cantidad_actual_nueva <= max_prestamo:
                cantidad_actual += 1
                libro_devuelto["cantidad_copias"] = cantidad_actual
                print(f"Libro '{titulo}' devuelto con éxito por {nombre}.")
            else:
                print(
                    f"Se ha superado el límite máximo de libros para '{titulo}'.")
        else:
            print(f"Libro '{titulo}' no pertenece a la biblioteca.")

    def listar_libros(self):
        """
        Muestra una lista de los libros en existencia.
        """
        if self.registro:
            print("Lista de Libros:")
            for id, nuevo_registro in self.registro.items():
                titulo = nuevo_registro["titulo"]
                cantidad_copias = nuevo_registro["cantidad_copias"]
                print(f"- {titulo}: {cantidad_copias}")
        else:
            print("No hay libros registrados.")


# Uso
gestor = GestorBiblioteca()

# Registrar libros
gestor.registro_libros(1, "Cien años de Soledad", "Garcia Marquez", 3, 3)
gestor.registro_libros(
    2, "Harry Potter: la píedra filosofal", "Jk Rowling", 3, 3)
gestor.registro_libros(
    3, "El señor de los anillos: la comunidad del anillo", "JRR Tolkien", 3, 2)

# Agregar usuario
gestor.agregar_usuario(1, "Sofia", 456789, "soo@soo.com")
gestor.agregar_usuario(2, "Juan", 456789, "juan@juan.com")

# Transaccion
gestor.prestamo_libro("Cien años de Soledad", "Sofia")
gestor.prestamo_libro("Cien años de Soledad", "Sofia")
gestor.prestamo_libro("Cien años de Soledad", "Juan")
gestor.prestamo_libro(
    "El señor de los anillos: la comunidad del anillo", "Lucas")
gestor.prestamo_libro("Harry Potter: la píedra filosofal", "Sofia")
gestor.prestamo_libro("Harry Potter: la píedra filosofal", "Juan")
gestor.prestamo_libro("Harry Potter: la píedra filosofal", "Juan")
gestor.prestamo_libro("Harry Potter: la píedra filosofal", "Juan")
gestor.devolucion_libro("Cien años de Soledad", "Sofia")
gestor.devolucion_libro("Cien años de Soledad", "Sofia")

# Lista
gestor.listar_libros()

# Gestor de Biblioteca con SRP
# Configurar Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)


class RegistroError(Exception):
    pass


class RegistroBiblioteca():
    def __init__(self):
        self.biblioteca = {}
        self.usuarios = {}

    def registro_libros(self, id, titulo, autor, cantidad_copias, max_prestamo):
        logger.debug("Iniciando el registro de un libro.")
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "cantidad_copias": cantidad_copias,
            "max_prestamo": max_prestamo
        }
        self.biblioteca[id] = nuevo_libro
        logger.info(f"Libro '{titulo}' agregado con éxito.")

    def registro_usuario(self, id, nombre, dni, email):
        logger.debug("Iniciando el registro de un usuario.")
        nuevo_usuario = {
            "nombre": nombre,
            "dni": dni,
            "email": email
        }
        self.usuarios[id] = nuevo_usuario
        logger.info(f"Usuario '{nombre}' agregado con éxito.")

    def verificacion_registro(self, tipo, titulo_o_nombre):
        logger.debug("Iniciando la verificación de un registro.")
        if tipo == "libro":
            for libro in self.biblioteca.values():
                if libro["titulo"] == titulo_o_nombre:
                    logger.info("Libro registrado")
                    return True
        elif tipo == "usuario":
            for usuario in self.usuarios.values():
                if usuario["nombre"] == titulo_o_nombre:
                    logger.info("Usuario registrado")
                    return True
        logger.error(f"{tipo.capitalize()} '{titulo_o_nombre}' no registrado")
        return False


class TransaccionBiblioteca():
    """
    Clase que gestiona las transacciones de prestamo y devolucion de una biblioteca.
    """

    def __init__(self, registro_biblioteca):
        self.registro_biblioteca = registro_biblioteca

    def prestamo_libro(self, titulo, nombre):
        logger.debug("Iniciando el prestamo de un libro.")
        try:
            if not self.registro_biblioteca.verificacion_registro("usuario", nombre):
                logger.error(f"Usuario '{nombre}' no está registrado.")
                return

            libro_prestado = None
            for id, nuevo_registro in self.registro_biblioteca.biblioteca.items():
                if nuevo_registro["titulo"] == titulo:
                    libro_prestado = nuevo_registro
                    logger.info("Coincidencia en la busqueda")
                    break
            if libro_prestado:
                if libro_prestado["cantidad_copias"] > 0:
                    libro_prestado["cantidad_copias"] -= 1
                    print(
                        f"Libro '{titulo}' prestado con éxito a {nombre}.")
                else:
                    logger.warning(
                        f"Libro '{titulo}' no tiene copias disponibles.")
            else:
                logger.error(f"Libro '{titulo}' no pertenece a la biblioteca.")
        except RegistroError as e:
            print(e)

    def devolucion_libro(self, titulo, nombre):
        logger.debug("Iniciando la devoluciòn de un libro.")
        try:
            if not self.registro_biblioteca.verificacion_registro("usuario", nombre):
                logger.error(f"Usuario '{nombre}' no está registrado.")
                return

            libro_devuelto = None
            for id, nuevo_registro in self.registro_biblioteca.biblioteca.items():
                if nuevo_registro["titulo"] == titulo:
                    libro_devuelto = nuevo_registro
                    logger.info("Coincidencia en la busqueda")
                    break
            if libro_devuelto:
                libro_devuelto["cantidad_copias"] += 1
                print(
                    f"Libro '{titulo}' devuelto con éxito por {nombre}.")
            else:
                logger.error(f"Libro '{titulo}' no pertenece a la biblioteca.")
        except RegistroError as e:
            print(e)


class Existencias():
    def __init__(self, registro_biblioteca):
        self.registro_biblioteca = registro_biblioteca

    def listar_libros(self):
        """
        Muestra una lista de los libros en existencia.
        """
        logger.debug("Recopilando los libros registrados en la biblioteca.")
        if self.registro_biblioteca.biblioteca:
            print("Lista de Libros:")
            for id, nuevo_registro in self.registro_biblioteca.biblioteca.items():
                titulo = nuevo_registro["titulo"]
                cantidad_copias = nuevo_registro["cantidad_copias"]
                print(f"- {titulo}: {cantidad_copias}")
        else:
            logger.warning("No hay libros registrados.")


# Uso
registro = RegistroBiblioteca()
transaccion = TransaccionBiblioteca(registro)
existencias = Existencias(registro)

# Registro libros
registro.registro_libros(1, "Cien años de Soledad", "Garcia Marquez", 3, 3)
registro.registro_libros(
    2, "Harry Potter: la piedra filosofal", "Jk Rowling", 3, 3)
registro.registro_libros(
    3, "El señor de los anillos: la comunidad del anillo", "JRR Tolkien", 3, 2)

# Registro usuarios
registro.registro_usuario(1, "Sofia", 456789, "soo@soo.com")
registro.registro_usuario(2, "Juan", 456789, "juan@juan.com")

# Transacciones
transaccion.prestamo_libro("Cien años de Soledad", "Sofia")
transaccion.prestamo_libro("Cien años de Soledad", "Sofia")
transaccion.prestamo_libro("Cien años de Soledad", "Juan")
transaccion.prestamo_libro("Harry Potter: la piedra filosofal", "Sofia")
transaccion.prestamo_libro("Harry Potter: la piedra filosofal", "Juan")
transaccion.devolucion_libro("Cien años de Soledad", "Sofia")
transaccion.devolucion_libro("Cien años de Soledad", "Sofia")

# Listar libros
existencias.listar_libros()
