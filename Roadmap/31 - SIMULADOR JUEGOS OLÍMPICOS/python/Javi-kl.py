from abc import ABC, abstractmethod
import random

print("""¡Los JJOO de París 2024 han comenzado!""")


class IRegistro(ABC):
    """Interfaz que define que hacer y NO como hacerlo
    guardar y obtener datos en el registro"""

    @abstractmethod
    def registrar(self, datos: str) -> bool:
        pass

    @abstractmethod
    def obtener_datos(self) -> list[str]:
        pass


# Modulos bajo nivel, solo guardan datos
class DatosEventos(IRegistro):
    def __init__(self):
        self.datos_eventos = []

    def registrar(self, dato: str) -> bool:
        self.datos_eventos.append(dato)
        return True

    def obtener_datos(self) -> list[str]:
        return self.datos_eventos


class DatosUsuarios(IRegistro):
    def __init__(self):
        self.datos_usuarios = []

    def registrar(self, dato: str) -> bool:
        self.datos_usuarios.append(dato)
        return True

    def obtener_datos(self) -> list[str]:
        return self.datos_usuarios


class ResultadosEventos(IRegistro):
    def __init__(self) -> None:
        self.resultados_list = []

    def registrar(self, dato: str) -> bool:
        self.resultados_list.append(dato)
        return True

    def obtener_datos(self) -> list[str]:
        return self.resultados_list


class Evento:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __str__(
        self,
    ) -> str:
        return f"Evento: {self.nombre}"


class Participante:
    def __init__(self, nombre, pais) -> None:
        self.nombre = nombre
        self.pais = pais

    def __str__(
        self,
    ) -> str:
        return f"Participante: {self.nombre}, Pais: {self.pais}"


class Resultado:
    def __init__(self, dato) -> None:

        self.evento = dato["evento"]
        self.oro = dato["medallas"][0]
        self.plata = dato["medallas"][1]
        self.bronce = dato["medallas"][2]

    def __str__(
        self,
    ) -> str:
        return f"{self.evento}\nOro: {self.oro}\nPlata: {self.plata}\nBronce: {self.bronce}"


class MedallaPais:
    """Representa UNA medalla ganada por UN país"""

    def __init__(self, pais, medalla) -> None:

        self.pais = pais
        self.medalla = medalla

    def __str__(
        self,
    ) -> str:
        return f"Pais: {self.pais}\nMedalla: {self.medalla}"


class SimuladorResultado:
    @staticmethod
    def simular(eventos, participantes):
        datos_simulaciones = []
        for evento in eventos:
            datos_evento = {}
            top3 = sorted(participantes, key=lambda x: random.random())
            datos_evento["evento"] = evento
            datos_evento["medallas"] = top3
            datos_simulaciones.append(datos_evento)
        return datos_simulaciones


class CalculadorMedallas:
    @staticmethod
    def calcular_medallas(todos_los_datos):
        solo_medallas = [
            dato for dato in todos_los_datos if isinstance(dato, MedallaPais)
        ]
        conteo_paises = {}
        for medalla in solo_medallas:
            pais = medalla.pais
            tipo = medalla.medalla
            if pais not in conteo_paises:
                conteo_paises[pais] = {"oro": 0, "plata": 0, "bronce": 0, "total": 0}
            conteo_paises[pais][tipo] += 1  # incrementa oro, plata o bronce
            conteo_paises[pais]["total"] += 1

        return sorted(
            conteo_paises.items(), key=lambda item: item[1]["total"], reverse=True
        )


# Informador
class Informador:
    """Modulo de alto nivel - muestra cualquier dato de los registros"""

    def __init__(self, registro: IRegistro):
        self.registro = registro

    def mostrar_datos(self):
        datos = self.registro.obtener_datos()
        for dato in datos:
            print(f"{dato}")


# Registrador
class Registrador:
    """Modulo de alto nivel -  registra cualquier cosa"""

    def __init__(self, registro: IRegistro):
        self.registro = registro

    def registrar_datos(self, datos):
        exito = self.registro.registrar(datos)
        if exito:
            print(f"Registrado con exito {datos}")
        else:
            print("Error al guardar")


# Eventos
datos_eventos = DatosEventos()
registrador_evento = Registrador(datos_eventos)

# Participantes
datos_participantes = DatosUsuarios()
registrador_participante = Registrador(datos_participantes)

# Simular resultados
simulador = SimuladorResultado()
calculador_medallas = CalculadorMedallas()
# Resultados
resultados = ResultadosEventos()
registrador_resultado = Registrador(resultados)

# Informador
informador_resultados = Informador(resultados)


# 6. Mostrar el ranking de países según el número de medallas.
def menu_principal():
    while True:
        print("Opciones:\n1. Registro de eventos.")
        print("2. Registro de participantes.")
        print("3. Simulación de eventos.")
        print("4. Creación de informes.")
        print("5. Salir del programa.")
        opcion = input("-> ")
        if opcion == "5":
            break

        elif opcion == "4":
            print(f"Informando de resultados")
            informador_resultados.mostrar_datos()
            """Ranking paises aqui"""
            todos_los_datos = resultados.obtener_datos()
            ranking = calculador_medallas.calcular_medallas(todos_los_datos)
            for posicion, (pais, medallas) in enumerate(ranking, start=1):
                print(f"{posicion}. {pais.upper()}")
                print(
                    f"  Oro: {medallas['oro']}, Plata: {medallas['plata']}, Bronce: {medallas['bronce']}"
                )
                print(f" Total: {medallas['total']}\n")

        elif opcion == "3":
            print("""\n¡Que comiencen los juegos!""")
            datos_simulacion = simulador.simular(
                datos_eventos.datos_eventos, datos_participantes.datos_usuarios
            )
            for dato in datos_simulacion:
                resultado = Resultado(dato)
                print("""\n¡Registrando resultado de los eventos!""")
                registrador_resultado.registrar_datos(resultado)
                medalla_oro = MedallaPais(pais=dato["medallas"][0].pais, medalla="oro")
                medalla_plata = MedallaPais(
                    pais=dato["medallas"][1].pais, medalla="plata"
                )
                medalla_bronce = MedallaPais(
                    pais=dato["medallas"][2].pais, medalla="bronce"
                )
                registrador_resultado.registrar_datos(medalla_oro)
                registrador_resultado.registrar_datos(medalla_plata)
                registrador_resultado.registrar_datos(medalla_bronce)

        elif opcion == "2":
            print("""\n¡Creando participante!""")
            nombre = input("Nombre participante -> ")
            pais = input("Pais ->")
            participante = Participante(nombre, pais)
            registrador_participante.registrar_datos(participante)

        elif opcion == "1":
            print("""\n¡Creando evento!""")
            nombre_evento = input("Nombre evento -> ")
            evento = Evento(nombre_evento)
            registrador_evento.registrar_datos(evento)

        else:
            print("Elije una opción valida...")


menu_principal()
