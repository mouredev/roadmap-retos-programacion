# EJERCICIO:
# ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
# ¿Alguien se entera de todas las relaciones de parentesco
# entre personajes que aparecen en la saga?
# Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
# Requisitos:
# 1. Estará formado por personas con las siguientes propiedades:
#    - Identificador único (obligatorio)
#    - Nombre (obligatorio)
#    - Pareja (opcional)
#    - Hijos (opcional)
# 2. Una persona solo puede tener una pareja (para simplificarlo).
# 3. Las relaciones deben validarse dentro de lo posible.
#    Ejemplo: Un hijo no puede tener tres padres.
# Acciones:
# 1. Crea un programa que permita crear y modificar el árbol.
#    - Añadir y eliminar personas
#    - Modificar pareja e hijo
# 2. Podrás imprimir el árbol (de la manera que consideres).
#
# NOTA: Ten en cuenta que la complejidad puede ser alta si
# se implementan todas las posibles relaciones. Intenta marcar
# tus propias reglas y límites para que te resulte asumible.


# ╔══════════════════════════════════════════════════╗
# ║ Autor:  Cristian Arenas                          ║
# ║ GitHub: https: https://github.com/cristianfloyd  ║
# ║ 2025 -  Python                                   ║
# ╚══════════════════════════════════════════════════╝

from abc import ABC
from typing import Literal, Optional, overload


class Persona:
    def __init__(
        self,
        person_id: int,
        nombre: str,
        pareja: Optional["Persona"] = None,
        hijos: Optional[list["Persona"]] = None,
    ):
        self.id = person_id
        self.nombre: str = nombre
        self.pareja: Optional["Persona"] = pareja or None
        self.hijos: list["Persona"] = hijos or []
        self.padres: tuple[Optional["Persona"], Optional["Persona"]] = (None, None)

    def accept_visitor(self, visitor: "ArbolVisitorInterface") -> None:
        visitor.visitar(self)

    def __str__(self):
        return f"{self.nombre} ({self.id})"

    def __repr__(self):
        return self.__str__()


class ArbolGenealogico:  # funcionará como repositorio de personas
    """Clase que representa el árbol genealógico"""

    def __init__(self):
        self.personas: dict[int, Persona] = {}
        self._proximo_id: int = 1

    def registrar_persona(self, nombre: str):
        """
        Registra una nueva persona en el arbol.

        Genera un identificador unico para la persona, valida el identificador y crea un nuevo objeto persona
        Args:
            nombre (str): El nombre a registrar.

        Raises:
            ValueError: Si el ID generado no es válido o se viola alguna restricción de validación.

        Returns:
            Persona: El objeto persona recién registrado.
        """
        nuevo_id = self._proximo_id
        try:
            validador = FamilyValidator(self.personas)
            validador.validar_id(nuevo_id)
            nueva_persona = Persona(nuevo_id, nombre)
            self.personas[nuevo_id] = nueva_persona
            self._proximo_id += 1
            return nueva_persona
        except ValueError as e:
            raise ValueError(f"Error al registrar persona: {e}")

    def init_get_root(self) -> list["Persona"]:
        """Buscamos en nuestro diccionario de personas aquellas que no tienen padres asignados."""
        return [
            p
            for p in self.personas.values()
            if p.padres[0] is None and p.padres[1] is None
        ]

    def get_persona(self, persona_id: int) -> "Persona":
        """Devuelve la persona con el ID especificado.
        Lanza ValueError si no existe.
        """
        if persona_id not in self.personas:
            raise ValueError(f"Persona con ID {persona_id} no encontrada")
        return self.personas[persona_id]

    def recorrer_arbol_completo(self, visitor: "ArbolVisitorInterface") -> None:
        """Refinamiento: El árbol sabe cómo ser recorrido íntegramente"""
        raices = self.init_get_root()
        for raiz in raices:
            raiz.accept_visitor(visitor)

    def add_hijo(self, padre: "Persona", hijo: "Persona") -> None:
        """Añade un hijo a una persona.
        
        Args:
            padre: La persona que será padre
            hijo: La persona que será hijo
            
        Raises:
            ValueError: Si la relación es inválida (ciclos, límite de padres, etc.)
            
        Example:
            >>> arbol = ArbolGenealogico()
            >>> padre = arbol.registrar_persona("Aenar")
            >>> hijo = arbol.registrar_persona("Gaemon")
            >>> arbol.add_hijo(padre, hijo)
        """
        try:
            validator = FamilyValidator(self.personas)
            validator.validar(padre, hijo, "hijo")
            padre.hijos.append(hijo)

            if hijo.padres[0] is None:
                hijo.padres = (padre, hijo.padres[1])
            elif hijo.padres[1] is None:
                hijo.padres = (hijo.padres[0], padre)

        except ValueError as e:
            raise ValueError(f"Error al añadir hijo: {e}")

    def add_pareja(self, persona1: "Persona", persona2: "Persona") -> None:
        """Añade una pareja a dos personas.
        Lanza ValueError si no es válido.
        """
        try:
            validator = FamilyValidator(self.personas)
            validator.validar(persona1, persona2, "pareja")
            persona1.pareja = persona2
            persona2.pareja = persona1
        except ValueError as e:
            raise ValueError(f"Error al añadir pareja: {e}")

    def remove_pareja(self, persona1: "Persona", persona2: "Persona") -> None:
        """Remueve una pareja de dos personas.
        Lanza ValueError si no es válido.
        """
        try:
            validator = FamilyValidator(self.personas)
            validator.validar(persona1, persona2, "remover_pareja")
            persona1.pareja = None
            persona2.pareja = None
        except ValueError as e:
            raise ValueError(f"Error al remover pareja: {e}")

    def eliminar_persona(self, persona_id: int, confirmar_rotura: bool = False) -> None:
        """Elimina una persona.
        Lanza ValueError si no es válido.
        """
        if persona_id not in self.personas:
            raise ValueError(f"Persona con ID {persona_id} no encontrada")

        persona = self.personas[persona_id]

        # chequear impacto eliminacion
        if persona.hijos and not confirmar_rotura:
            validador = FamilyValidator(self.personas)
            validador.validar_impacto_eliminacion(persona)

        # 1 desvincular la pareja
        if persona.pareja:
            persona.pareja.pareja = None
            persona.pareja = None
        # 2 desvincular los padres
        for p in persona.padres:
            if p:
                p.hijos.remove(persona)

        # 3 desvincular los hijos
        for h in persona.hijos:
            p_lista: list[Persona | None] = list(h.padres)
            if p_lista[0] and p_lista[0].id == persona.id:
                p_lista[0] = None
            if p_lista[1] and p_lista[1].id == persona.id:
                p_lista[1] = None
            h.padres = (p_lista[0], p_lista[1])

        # 4 eliminar la persona
        del self.personas[persona_id]



class FamilyValidator:  # funcionará como validador de relaciones
    """Clase que valida las relaciones entre personas"""

    def __init__(self, personas_existentes: dict[int, "Persona"]):
        self.personas_existentes: dict[int, "Persona"] = personas_existentes

    def validar(self, persona1: "Persona", persona2: "Persona", relacion: str):
        match relacion:
            case "nuevo_registro":
                pass
            case "eliminar_persona":
                self.validar_impacto_eliminacion(persona1)
            case "pareja":
                self._validar_pareja(persona1, persona2)
            case "remover_pareja":
                self._validar_remover_pareja(persona1, persona2)
            case "hijo":
                self._validar_hijo(persona1, persona2)
            case _:
                raise ValueError("Relacion no valida")

    def _validar_hijo(self, padre: "Persona", hijo: "Persona"):
        # regla 1: no puede ser su propio padre
        if padre.id == hijo.id:
            raise ValueError(f"{padre.nombre} no puede ser su propio padre")
        # regla 2: maximo 2 padres
        self._limite_padres(hijo)

        # regla 3: no puede ser pareja de su propio padre
        self._no_pareja_descendiente(hijo, padre)

        # regla 4: deteccion de ciclos, ej.:
        # A es hijo de B, B es hijo de C, C es hijo de A.
        # No crear bucles infinitos
        self._deteccion_ciclos(hijo, padre)

    def _limite_padres(self, persona: "Persona") -> None:
        """
        Valida que la persona no tenga más de 2 padres.
        Args:
            persona: La persona a validar
        Raises:
            ValueError: Si la persona ya tiene 2 padres
        """
        if persona.padres[0] is not None and persona.padres[1] is not None:
            raise ValueError("La persona ya tiene 2 padres")

    def _no_pareja_descendiente(self, hijo: "Persona", padre: "Persona") -> None:
        """
        Valida que el hijo no sea pareja de su propio padre.
        Args:
            hijo: La persona que será hijo
            padre: La persona que será padre
        Raises:
            ValueError: Si la relación es inválida (ciclos, límite de padres, etc.)
        """
        if hijo.pareja is not None and hijo.pareja.id == padre.id:
            raise ValueError(f"{hijo.nombre} no puede ser pareja de su propio padre")
        if padre.pareja is not None and padre.pareja.id == hijo.id:
            raise ValueError(f"{padre.nombre} no puede ser pareja de su propio hijo")

    def _deteccion_ciclos(self, hijo: "Persona", padre: "Persona"):
        """
        Funcion recursiva que detecta ciclos en el arbol genealógico
        """
        if self._es_ancestro_de(hijo, padre):
            raise ValueError(
                f"¡Paradoja temporal! {hijo.nombre} es ancestro de {padre.nombre}."
            )

    def _es_ancestro_de(self, buscar: "Persona", inicio: "Persona") -> bool:
        """
        sube por el arbol desde 'inicio' buscando a 'buscar'
        """
        # Si no, busca recursivamente en los padres de los padres.
        for p in inicio.padres:
            if p is not None:
                if p.id == buscar.id or self._es_ancestro_de(buscar, p):
                    return True
        return False

    def validar_id(self, id_nuevo: Optional[int]):
        if id_nuevo is None:
            raise ValueError("El id no puede ser nulo")

        if id_nuevo <= 0:
            raise ValueError(f"El id {id_nuevo} debe ser un entero positivo")

        if id_nuevo in self.personas_existentes:
            raise ValueError(f"El id {id_nuevo} ya pertenece a otra persona")

    def _validar_pareja(self, persona1: "Persona", persona2: "Persona") -> None:
        """Valida que persona1 y persona2 sean parejas
        Args: persona1, persona2 (Persona)
        """
        if persona1.id == persona2.id:
            raise ValueError(f"{persona1.nombre} no puede ser su propia pareja")

        if persona1.pareja is not None:
            raise ValueError(
                f"{persona1.nombre} ya tiene una pareja: {persona1.pareja.nombre}."
            )
        if persona2.pareja is not None:
            raise ValueError(
                f"{persona2.nombre} ya tiene una pareja: {persona2.pareja.nombre}."
            )

    def _validar_remover_pareja(self, persona1: "Persona", persona2: "Persona") -> None:
        try:
            if persona1.pareja is None or persona2.pareja is None:
                raise ValueError(
                    f"{persona1.nombre} o {persona2.nombre} no tiene pareja"
                )
            if persona1.pareja.id != persona2.id:
                raise ValueError(
                    f"{persona1.nombre} y {persona2.nombre} no son parejas"
                )
            if persona2.pareja.id != persona1.id:
                raise ValueError(
                    f"{persona1.nombre} y {persona2.nombre} no son parejas"
                )
        except ValueError as e:
            raise ValueError(f"Error al validar remover pareja: {e}")

    @staticmethod
    def validar_impacto_eliminacion(persona: "Persona") -> None:
        if persona.hijos:
            raise ValueError(
                f"ADVERTENCIA: {persona.nombre} tiene descendientes. "
                "Eliminar este nodo dividirá el árbol en dos y romperá el linaje. "
                "¿Desea continuar?"
            )


class ArbolVisitorInterface(ABC):  # patron visitor
    """Clase que representa un visitante del árbol genealógico
    - Interfaz
    """

    def visitar(self, persona: "Persona"):
        pass


class PrintArbolVisitor(ArbolVisitorInterface):  # patron visitor concreto
    """Clase que representa un visitante del árbol genealógico que imprimira el árbol
    - Su estado interno es el string que está construyendo
    - Utiliza recursividad para añadir └— y ├—.
    """

    def __init__(self):
        self.resultado: list[str] = []
        self.visitados: set[int] = set()

    def visitar(self, persona: "Persona"):
        """
        Visita una persona y sus hijos de manera recursiva.
        Args:
            persona (Persona): La persona a visitar.
        """
        if persona.id not in self.visitados:
            # inicia el recorrido desde esta persona como raiz.
            self._visitar_recursivo(persona, es_ultimo=True, prefijos=[])

    def _visitar_recursivo(self, persona: "Persona", es_ultimo: bool, prefijos: list[str]):
        """
        Metodo auxiliar recursivo que realiza la impresion real.
        Args:
            persona (Persona): La persona a visitar.
            es_ultimo (bool): Indica si es el ultimo hijo de su padre.
            prefijos (list[str]): Prefijos para la impresion.
        """
        if persona.id in self.visitados:
            return
        
        # construir el prefijo concatenando los prefijos
        prefijo_completo = "".join(prefijos)

        # Elegir símbolo: └─ para último hijo, ├─ para hijos intermedios
        simbolo = "└─" if es_ultimo else "├─"
    
        # Construir la línea con información de la persona
        persona_id = f" (id: {persona.id})" if persona.id else ""
        pareja_str = f"-> {persona.pareja.id}" if persona.pareja else ""

        self.resultado.append(f"{prefijo_completo}{simbolo} {persona.nombre}{persona_id}{pareja_str}")
        self.visitados.add(persona.id)

        # hijos que aun no han sido visitados
        hijos_no_visitados = [h for h in persona.hijos if h.id not in self.visitados]

        # recorrer hijos no visitados
        for i, hijo in enumerate(hijos_no_visitados):
            es_ultimo_hijo = i == len(hijos_no_visitados) - 1

            # crear prefijos para el siguiente nivel
            nuevos_prefijos = prefijos.copy()
            nuevo_prefijo =  "│  " if not es_ultimo else "   "

            nuevos_prefijos.append(nuevo_prefijo)

            # llamada recursiva
            self._visitar_recursivo(hijo, es_ultimo_hijo, nuevos_prefijos)
    

    def ejecutar(self, persona: "Persona"):
        self.visitar(persona)
        return "\n".join(self.resultado)

    def get_resultado(self):
        if not self.resultado:
            return "No hay personajes registrados."
        return "\n".join(self.resultado)


class SearchArbolVisitor(ArbolVisitorInterface):  # patron visitor concreto
    """Clase que representa un visitante del árbol genealógico que buscara una persona
    - Su estado es el resultado de la búsqueda.
    - No imprime nada, solo acumula nodos que cumplan un criterio.
    """

    def __init__(self, nombre_a_buscar: str):
        self.resultado: list["Persona"] = []
        self.nombre_a_buscar: str = nombre_a_buscar.strip().lower()
        self.visitados: set[int] = set()

    def visitar(self, persona: "Persona"):
        if persona.id in self.visitados:
            return
        
        self.visitados.add(persona.id)

        if persona.nombre.strip().lower() == self.nombre_a_buscar:
            self.resultado.append(persona)

        for hijo in persona.hijos:
            hijo.accept_visitor(self)

    def obtener_resultado(self):
        """
        Returns the result stored in the object.
        Retorna el resultado almacenado en el objeto.

        Este método recupera el valor del resultado almacenado internamente en el
        objeto. No modifica ni altera el valor almacenado y sirve como un simple
        accessor.

        Returns:
            list[Persona]: Lista de personas que cumplen con el criterio de búsqueda.
        """
        return self.resultado


class DinastiaUI:
    def __init__(self, arbol_gen: "ArbolGenealogico") -> None:
        self.arbol = arbol_gen

    def mostrar_menu_principal(self):
        while True:
            print("\nMenu Principal")
            print("1. Agregar persona")
            print("2. Eliminar persona")
            print("3. Buscar persona")
            print("4. Mostrar arbol")
            print("5. Agregar hijo")
            print("6. Agregar pareja")
            print("7. Eliminar pareja")
            print("8. Salir")
            opcion = input("Ingrese una opción: ").strip().lower()

            match opcion:
                case "1":
                    self.agregar_persona()
                case "2":
                    self.eliminar_persona()
                case "3":
                    self.buscar_persona()
                case "4":
                    self.mostrar_arbol()
                case "5":
                    self.agregar_hijo()
                case "6":
                    self.agregar_pareja()
                case "7":
                    self.eliminar_pareja()
                case "8":
                    break
                case _:
                    print("Opción invalida. Intente de nuevo.")

    def agregar_persona(self):
        try:
            nombre = self.pedir_dato(
                mensaje="Ingrese el nombre de la persona: ", es_entero=False
            )
            nuevo_registro = self.arbol.registrar_persona(nombre)
            print(f"Persona {nuevo_registro.nombre} registrada exitosamente.")
            print(f"\nID: {nuevo_registro.id}")
        except ValueError as e:
            print(e)

    def buscar_persona(self):
        try:
            print("Ingrese el nombre de la persona a buscar:")
            nombre = self.pedir_dato(mensaje="Nombre: ", es_entero=False)
            visitor = SearchArbolVisitor(nombre)
            self.arbol.recorrer_arbol_completo(visitor)
            resultados = visitor.obtener_resultado()
            if not resultados:
                print("No se encontraron resultados.")
            else:
                print("Resultados:")
                for r in resultados:
                    print(f"- {r.nombre} ({r.id})")
        except ValueError as e:
            print(e)

    def mostrar_arbol(self):
        """Muestra el arbol genealógico via visitor; maneja arbol vacío"""
        try:
            visitor = PrintArbolVisitor()
            self.arbol.recorrer_arbol_completo(visitor)
            resultado = visitor.get_resultado()
            print(resultado)
        except ValueError as e:
            print(e)

    def agregar_hijo(self):
        try:
            padre_id = self.pedir_dato("Ingrese el ID del padre: ", True)
            hijo_id = self.pedir_dato("Ingrese el ID del hijo: ", True)

            padre = self.arbol.get_persona(padre_id)
            hijo = self.arbol.get_persona(hijo_id)

            self.arbol.add_hijo(padre, hijo)
            print(f"Ahora {padre.nombre} es padre de {hijo.nombre}")
        except ValueError as e:
            print(f"Error: {e}")

    def agregar_pareja(self):
        try:
            persona1_id = self.pedir_dato(
                mensaje="Ingrese el ID de la primera persona: ", es_entero=True
            )
            persona2_id = self.pedir_dato(
                mensaje="Ingrese el ID de la segunda persona: ", es_entero=True
            )

            persona1 = self.arbol.get_persona(persona1_id)
            persona2 = self.arbol.get_persona(persona2_id)
            self.arbol.add_pareja(persona1, persona2)
            print(f"Ahora {persona1.nombre} es pareja de {persona2.nombre}")
        except ValueError as e:
            print(f"Error: {e}")

    @overload
    @staticmethod
    def pedir_dato(mensaje: str, es_entero: Literal[True]) -> int: ...

    @overload
    @staticmethod
    def pedir_dato(mensaje: str, es_entero: Literal[False]) -> str: ...

    @staticmethod
    def pedir_dato(mensaje: str, es_entero: bool = False) -> None | str | int:
        """
        Pide un dato al usuario.
        Args:
            mensaje (str): El mensaje a mostrar al usuario.
            es_entero (bool): Indica si el dato debe ser un entero.
        Returns:
            None | str | int: El dato ingresado por el usuario.
        """
        while True:
            dato = input(mensaje).strip()
            if not dato:
                print("El valor no puede estar vacío. Intente de nuevo.")
                continue
            if es_entero:
                try:
                    return int(dato)
                except ValueError:
                    print("El valor debe ser un entero. Intente de nuevo.")
                    continue
            return dato

    def eliminar_pareja(self):
        try:
            persona1_id = self.pedir_dato("Ingrese el ID de la primera persona: ", True)
            persona2_id = self.pedir_dato("Ingrese el ID de la segunda persona: ", True)
            persona1 = self.arbol.get_persona(persona1_id)
            persona2 = self.arbol.get_persona(persona2_id)
            self.arbol.remove_pareja(persona1, persona2)
            print(f"Ahora {persona1.nombre} no es pareja de {persona2.nombre}")
        except ValueError as e:
            print(f"Error: {e}")

    def eliminar_persona(self):
        try:
            id_persona = self.pedir_dato(
                "Ingrese el ID de la persona a eliminar: ", True
            )
            persona = self.arbol.get_persona(id_persona)
            try:
                self.arbol.eliminar_persona(id_persona)
                print(f"Persona {persona.nombre} eliminada exitosamente.")
            except ValueError as e:
                mensaje_error = str(e)
                if "ADVERTENCIA" in mensaje_error:
                    print(f"\n{mensaje_error}")
                    confirma = input("Desea continuar? (s/n): ").strip().lower()
                    if confirma == "s":
                        confirma = True
                        self.arbol.eliminar_persona(id_persona, confirma)
                        print(f"Persona {persona.nombre} eliminada exitosamente.")
                    else:
                        print("Operación cancelada.")
                else:
                    print(f"Error: {e}")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    arbol = ArbolGenealogico()
    aenar = arbol.registrar_persona("Aenar")

    gaemon = arbol.registrar_persona("Gaemon")
    daenys = arbol.registrar_persona("Daenys")
    arbol.add_hijo(aenar, gaemon)
    arbol.add_hijo(aenar, daenys)
    arbol.add_pareja(gaemon, daenys)

    aegon = arbol.registrar_persona("Aegon")
    eleana = arbol.registrar_persona("Elaena")
    arbol.add_pareja(aegon, eleana)

    arbol.add_hijo(gaemon, aegon)
    arbol.add_hijo(daenys, aegon)

    arbol.add_hijo(gaemon, eleana)
    arbol.add_hijo(daenys, eleana)

    maegon = arbol.registrar_persona("Maegon")
    aerys = arbol.registrar_persona("Aerys")

    arbol.add_hijo(eleana, maegon)
    arbol.add_hijo(aegon, maegon)
    arbol.add_hijo(eleana, aerys)
    arbol.add_hijo(aegon, aerys)

    ui = DinastiaUI(arbol)
    ui.mostrar_menu_principal()
