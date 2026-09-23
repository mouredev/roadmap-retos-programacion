# EJERCICIO:
# Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
# implemente una superclase Animal y un par de subclases Perro y Gato,
# junto con una función que sirva para imprimir el sonido que emite cada Animal.

class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
            self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def hacer_ruido(self):
            return "*sonidos de animal*"

class Perro(Animal):
     def __init__(self, nombre, edad):
          super().__init__(nombre, edad)

     def hacer_ruido(self):
          return "*woof*"

class Gato(Animal):
     def __init__(self, nombre, edad):
          super().__init__(nombre, edad)

     def hacer_ruido(self):
          return "*miau*"

animal_desconocido = Animal('Unknown', 20)
michi = Gato('Michi', 10)
bianca = Perro('Bianca', 5)

print("Animales registrados:")
print(f"1. {animal_desconocido.get_nombre()} | {animal_desconocido.get_edad()} años")
print(f"2. {michi.get_nombre()} | {michi.get_nombre()} años")
print(f"3. {bianca.get_nombre()} | {bianca.get_nombre()} años")

print("\nSonidos registrados:")
print(f"1. {animal_desconocido.get_nombre()}: {animal_desconocido.hacer_ruido()}")
print(f"2. {michi.get_nombre()}: {michi.hacer_ruido()}")
print(f"3. {bianca.get_nombre()}: {bianca.hacer_ruido()}")

# DIFICULTAD EXTRA (opcional):
# Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
# pueden ser Gerentes, Gerentes de Proyectos o Programadores.
# Cada empleado tiene un identificador y un nombre.
# Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
# actividad, y almacenan los empleados a su cargo.

class Empleado:
     def __init__(self, id: str, nombres: str, apellidos: str):
          self.__id = id
          self.__nombres = nombres
          self.__apellidos = apellidos

     def get_id(self):
          return self.__id

     def get_nombres(self):
          return self.__nombres

     def get_apellidos(self):
          return self.__apellidos

     def get_nombre_completo(self):
          return f"{self.get_nombres()} {self.get_apellidos()}"

     def set_nombres(self, nombres):
          self.__nombres = nombres

     def set_apellidos(self, apellidos):
          self.__apellidos = apellidos

     def trabajar(self):
          return '*trabajando*'

class Gerente(Empleado):
     def __init__(self, id: str, nombres: str, apellidos :str,
                  empleados: set = set()):
          super().__init__(id, nombres, apellidos)
          self.__empleados = empleados

     def get_empleados(self):
          return self.__empleados

     def agregar_empleado(self, empleado: Empleado):
          self.__empleados.add(empleado)

     def quitar_empleado(self, id: str):
          for empleado in self.get_empleados():
               if empleado.get_id() == id:
                    self.__empleados.remove(empleado)
                    break

     def trabajar(self):
          return '*haciendo cosas de gerente*'

class GerenteProyecto(Gerente):
     def __init__(self, id: str, nombres: str, apellidos: str,
                  empleados: set = set(),
                  proyectos: set = set()):
          super().__init__(id, nombres, apellidos, empleados)
          self.__proyectos = proyectos

     def get_proyectos(self):
          return self.__proyectos

     def agregar_proyecto(self, proyecto: str):
          self.__proyectos.add(proyecto)

     def quitar_proyecto(self, proyecto: str):
          for proy in self.get_proyectos():
               if proy == proyecto:
                    self.__proyectos.remove(proyecto)
                    break

     def trabajar(self):
          return '*dirigiendo proyecto*'

     def iniciar_proyecto(self):
          return '*iniciando proyecto*'

     def pausar_proyecto(self):
          return '*pausando proyecto*'

     def continuar_proyecto(self):
          return '*continuando proyecto*'

     def terminar_proyecto(self):
          return '*terminando proyecto*'
     
     def cancelar_proyecto(self):
          return '*cancelando proyecto*'

class Programador(Empleado):
     def __init__(self, id: str, nombres: str, apellidos: str,
                  tecnologias: set = set()):
          super().__init__(id, nombres, apellidos)
          self.__tecnologias = tecnologias

     def get_tecnologias(self):
          return self.__tecnologias

     def agregar_tecnologia(self, tecnologia: str):
          self.__tecnologias.add(tecnologia)

     def quitar_tecnologia(self, tecnologia: str):
          for tecno in self.get_tecnologias():
               if tecno == tecnologia:
                    self.__tecnologias.remove(tecnologia)
                    break

     def trabajar(self):
          return '*tecleteando intensamente*'

print("\n=== EMPRESA SIN NOMBRE ===")

programador_python = Programador('1090', 'Gabriel', 'Feliciano Bacca',
                                 tecnologias = {'Python'})
programador_java = Programador('1091', 'Halo', 'Cortéz Laverian',
                               tecnologias = {'Java', 'Kotlin'})
programador_senior = Programador('1092', 'Gabriela', 'Valderrama Arica',
                                 tecnologias = {'Python', 'Java', 'Python',
                                                'SQL Server', 'MySQL', 'MongoDB'})
programador_junior = Programador('1093', 'Diego Jesús', 'Goméz Perea')
otro_programador_junior = Programador('1094', 'Claudia', 'Contreras Despoux')

gerente_de_proyecto_python = GerenteProyecto('1050', 'Leandro', 'Huanuqueño Bacca',
                                             empleados = {programador_python,
                                                          programador_java},
                                             proyectos = {'Proyecto Python #1'})
gerente_de_proyecto_java = GerenteProyecto('1051', 'Mary Ann', 'Guadalupe Valderrama',
                                           empleados = {programador_senior,
                                                        programador_junior,
                                                        otro_programador_junior})

gerente_general = Gerente('1000', 'Ted', 'Contreras Torrejón', empleados = {
     programador_python, programador_java, programador_senior,
     programador_junior, otro_programador_junior,
     gerente_de_proyecto_python, gerente_de_proyecto_java
})

print("\nPersonal:")
print(f"> GERENTE GENERAL: {gerente_general.get_nombre_completo()} "
      f"(ID: {gerente_general.get_id()})")
for empleado in gerente_general.get_empleados():
     if isinstance(empleado, Programador):
          print("> Programador: ", end="")
     elif isinstance(empleado, GerenteProyecto):
          print("> Gerente de Proyectos: ", end="")
     else:
          print("> Empleado: ", end="")
     print(f"{empleado.get_nombre_completo()} (ID: {empleado.get_id()})")

print(f"\n{gerente_de_proyecto_java.get_nombre_completo()}: "
      f"{gerente_de_proyecto_java.trabajar()}")
print("Nuevo proyecto Java establecido. "
      "Se requiere que todos los programadores conozcan 'Java'.")

for empleado in gerente_de_proyecto_java.get_empleados():
     if isinstance(empleado, Programador):
          empleado.agregar_tecnologia('Java')

print("\nRevisando conocimiento de programadores: ")
for empleado in gerente_de_proyecto_java.get_empleados():
     if isinstance(empleado, Programador):
          print(f"{empleado.get_nombre_completo()}: {empleado.get_tecnologias()}")

print(f"\n{gerente_de_proyecto_java.get_nombre_completo()}: "
      f"{gerente_de_proyecto_java.iniciar_proyecto()}")
print("Nuevo proyecto Java iniciado.")

print(f"\n{gerente_general.get_nombre_completo()}: "
      f"{gerente_general.trabajar()}")
print(f"{gerente_de_proyecto_python.get_nombre_completo()}: "
      f"{gerente_de_proyecto_python.trabajar()}")

print("Nuevo proyecto Python establecido. "
      "Se requiere que todos los programadores conozcan 'Python'.")

print("\nRevisando conocimiento de programadores: ")
for empleado in gerente_de_proyecto_python.get_empleados():
     if isinstance(empleado, Programador):
          print(f"{empleado.get_nombre_completo()}: {empleado.get_tecnologias()}")

print("\nNo todos los programadores conocen 'Python'. Se cancela proyecto.")
print(f"{gerente_de_proyecto_python.get_nombre_completo()}: "
      f"{gerente_de_proyecto_python.cancelar_proyecto()}")
print("Nuevo proyecto Python cancelado.")

print(f"\n{gerente_de_proyecto_java.get_nombre_completo()}: "
      f"{gerente_de_proyecto_java.continuar_proyecto()}")
for empleado in gerente_de_proyecto_java.get_empleados():
     if isinstance(empleado, Programador):
          print(f"{empleado.get_nombre_completo()}: {empleado.trabajar()}")

print("\nAVISO: Se encontraron problemas en el proyecto Java. "
      "Se solicita inspección.")
print(f"{gerente_de_proyecto_java.get_nombre_completo()}: "
      f"{gerente_de_proyecto_java.pausar_proyecto()}")

print("\nAVISO: Inspección de proyecto Java terminada. Proceder a todo máquina.")
print(f"{gerente_de_proyecto_java.get_nombre_completo()}: "
      f"{gerente_de_proyecto_java.continuar_proyecto()}")
for empleado in gerente_de_proyecto_java.get_empleados():
     if isinstance(empleado, Programador):
          print(f"\n{empleado.get_nombre_completo()}: {empleado.trabajar()}" * 5)

print(f"\n{gerente_de_proyecto_java.get_nombre_completo()}: "
      f"{gerente_de_proyecto_java.terminar_proyecto()}")
print("AVISO: Proyecto Java concluido. Buen trabajo a todos.")

gerente_de_proyecto_java.agregar_proyecto('Proyecto Java #1')

print(f"\nRevisando proyectos de este mes...")
for empleado in gerente_general.get_empleados():
     if isinstance(empleado, GerenteProyecto):
          print(f"{empleado.get_nombre_completo()}: {empleado.get_proyectos()}")

print("\nAVISO: Empleado no registrado accedió al sistema...")
hacker = Empleado('0001', 'El', 'Anonymous')
print(f"Datos encontrados: {hacker.get_nombre_completo()} (ID: {hacker.get_id()})")
print(f"Últimas acciones del Hacker: {hacker.trabajar()} {hacker.trabajar()}")

print("\nAVISO: Hacker se está haciendo pasar por otro empleado")
hacker.set_nombres('Gabriel')
hacker.set_apellidos('Feliciano Bacca')

print(f"\nAVISO: Si encuentra un empleado de nombre "
      f"'{hacker.get_nombres()} {hacker.get_apellidos()}' "
      f"verificar su ID. Si es '{hacker.get_id()}' debe reportarlo.")

print(f"\nAVISO: Hacker accedió a la base de datos principal. "
      "\nY ha hecho las siguientes acciones:")
print("> Infiltrarse en los equipos de programadores.")
gerente_de_proyecto_java.agregar_empleado(hacker)
gerente_de_proyecto_java.agregar_empleado(hacker)
gerente_general.agregar_empleado(hacker)

print("> Eliminar registros de proyectos.")
gerente_de_proyecto_java.quitar_proyecto("Proyecto Java #1")
gerente_de_proyecto_python.quitar_proyecto("Proyecto Python #1")

print("> Eliminar al empleado al que le robó su identidad del sistema.")
gerente_general.quitar_empleado('1090')
gerente_de_proyecto_python.quitar_empleado('1090')

print("> Eliminar registros de un programador senior.")
for tecnologia in programador_senior.get_tecnologias().copy():
     programador_senior.quitar_tecnologia(tecnologia)

print("> Registrar falsos proyectos.")
gerente_de_proyecto_java.agregar_proyecto("Proyecto de la carita de Pacman :v")
gerente_de_proyecto_python.agregar_proyecto("Proyecto del XD")

print("\nAVISO: Se imprimirá en pantalla todos los registros actuales "
      "para identificar información falsa y/o faltante.")

print("\nPersonal:")
print(f"> GERENTE GENERAL: {gerente_general.get_nombre_completo()} "
      f"(ID: {gerente_general.get_id()})")
for empleado in gerente_general.get_empleados():
     if isinstance(empleado, Programador):
          print("> Programador: ", end="")
     elif isinstance(empleado, GerenteProyecto):
          print("> Gerente de Proyectos: ", end="")
     else:
          print("> Empleado: ", end="")
     print(f"{empleado.get_nombre_completo()} (ID: {empleado.get_id()})")

print("\nConocimientos de programadores:")
for empleado in gerente_general.get_empleados():
     if isinstance(empleado, Programador):
          print(f"> {empleado.get_nombre_completo()}: {empleado.get_tecnologias()}")

print("\nProyectos:")
for proyecto in (gerente_de_proyecto_java.get_proyectos()
                 | gerente_de_proyecto_python.get_proyectos()):
     print(f"> {proyecto}")

print("\nAVISO: El equipo de seguridad ya está en busca del hacker. "
      "Harán el aviso tan pronto lo atrapen.")
print("FIN DE REPORTE")

print(f"\n{hacker.get_nombre_completo()}: {hacker.trabajar()} {hacker.trabajar()}")