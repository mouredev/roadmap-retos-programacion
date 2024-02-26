"""
 EJERCICIO:
 Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 atributos y una función que los imprima (teniendo en cuenta las posibilidades
 de tu lenguaje).
 Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 utilizando su función.

 DIFICULTAD EXTRA (opcional):
 Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 en el ejercicio número 7 de la ruta de estudio)
 - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
   retornar el número de elementos e imprimir todo su contenido.
"""


class LinearStructure:

    def __init__(self, tipo: str):
        self.tipo = tipo.upper()
        self.elementos = []
        if not self.validate():
            raise TypeError(f"Los stack solo pueden ser de tipo PILA o tipo COLA => {tipo} NO es válido.")

    def put(self, elemento) -> None:
        self.elementos.append(elemento)

    def take(self) -> object:
        if self.elementos.__len__():
            if self.tipo == "PILA":
                elemento = self.elementos.pop()
            else:
                elemento = self.elementos.pop(0)
            return elemento
        return None

    def __len__(self):
        return self.elementos.__len__()

    def __str__(self):
        return f"{self.tipo} contiene {self.__len__()} elementos."

    def clear(self):
        self.elementos.clear()

    def validate(self) -> bool:
        return self.tipo in ("PILA", "COLA")


def anonymous_block(function):
    titulo = function.__name__.replace('_', ' ').title()
    print(f"\nBEGIN {titulo}:\n")
    function()
    print(f"\nEND {titulo}\n")


@anonymous_block
def explicacion():
    print("""Las clases proveen una forma de empaquetar datos y funcionalidad juntos. Al crear una nueva clase, se crea un nuevo tipo de objeto,
    permitiendo crear nuevas instancias de ese tipo. Cada instancia creada en base a esta clase heredará todos sus atributos y métodos que, a su vez
    los puede reimplementar y/o agregar nuevos.
    
    Como ejemplo creamos la clase LinearStructure (que permite implementar pilas y colas) la cual re-implementa los métodos "__len__" y "__str__". 
    Luego implementaremos una clase "Navegador" que, sobre los métodos heredados de LinearStructure, redefine validate y va a agragar un método 
    extra "get_top".
    Tambien vamos a impementar una clase PrintSpooler que hereda LinearStructure, redefine validate y crea métodos propios.

    class LinearStructure:

        def __init__(self, tipo: str):
            self.tipo = tipo.upper()
            self.elementos = []
            if not self.validate():
                raise TypeError(f"Los stack solo pueden ser de tipo PILA o tipo COLA => {tipo} NO es válido.")

        def put(self, elemento) -> None:
            self.elementos.append(elemento)

        def take(self) -> object:
            if self.elementos.__len__():
                if self.tipo == "PILA":
                    elemento = self.elementos.pop()
                else:
                    elemento = self.elementos.pop(0)
                return elemento
            return None

        def __len__(self):
            return self.elementos.__len__()

        def __str__(self):
            return f"{self.tipo} contiene {self.__len__()} elementos."

        def clear(self):
            self.elementos.clear()

        def validate(self) -> bool:
            return self.tipo in ("PILA", "COLA"))
    
    class Navegador(LinearStructure):
        def __init__(self, tipo):
            super().__init__(tipo)
    
        def get_top(self) -> object:
            if self.tipo == "PILA":
                return self.elementos[-1]
            if self.tipo == "PILA":
                return self.elementos[0]

    class PrintSpooler(LinearStructure):
        def __init__(self, tipo):
            super().__init__(tipo)
            if not self.validate():
                raise TypeError(f"Solo puede instanciar COLA.")

        def print_doc(self) -> None:
            print(f"Printing {self.take()}")

        def print_all(self) -> None:
            while self.elementos:
                self.print_doc()

        def remove_doc(self, doc_idx: int):
            if doc_idx == 0:
                print(f"Doc {self.elementos[0]} is Ready To Print => can't be removed.")
            else:
                print(f"Removig {self.elementos.pop(doc_idx)}")

        def list_spool(self):
            for index, doc in enumerate(self.elementos):
                if index == 0:
                    print(f"Document {doc} is ready to print.")
                else:
                    print(f"Document {doc} is waiting for ({index}) document to print.")

        def validate(self):
            return self.tipo == "COLA"

    pila_atras = Navegador("PILA")
    pila_adelante = Navegador("PILA")
    spooler = PrintSpooler("COLA")
    """)


@anonymous_block
def dificultad_extra_navegar():
    class Navegador(LinearStructure):
        def __init__(self, tipo):
            super().__init__(tipo)
            if not self.validate():
                raise TypeError(f"Solo puede instanciar PILA.")

        def get_top(self) -> object:
            return self.elementos[-1]

        def validate(self):
            return self.tipo == "PILA"

    pila_atras = Navegador("PILA")
    pila_adelante = Navegador("PILA")
    boton_adelante = False
    boton_atras = False

    def navegar(opcion: str) -> str:
        nonlocal pila_atras
        nonlocal pila_adelante
        nonlocal boton_atras
        nonlocal boton_adelante

        if opcion == "atras" and boton_atras:
            pagina = pila_atras.take()
            pila_adelante.put(pagina)
            pagina = pila_atras.get_top()
            print(f"Vuelvo a {pagina}")
        elif opcion == "adelante" and boton_adelante:
            pagina = pila_adelante.take()
            pila_atras.put(pagina)
            print(f"Voy a {pagina}")
        else:
            if opcion not in ("atras", "adelante"):
                pagina = opcion
                pila_adelante.clear()
                pila_atras.put(pagina)
            else:
                pagina = pila_atras.get_top()

        return pagina

    def habilitar_botones() -> None:
        nonlocal pila_atras
        nonlocal pila_adelante
        nonlocal boton_atras
        nonlocal boton_adelante

        if pila_atras.__len__() > 1:
            boton_atras = True
        else:
            boton_atras = False
        if pila_adelante:
            boton_adelante = True
        else:
            boton_adelante = False

    salto = "\n"
    habilitar_botones()
    while True:
        menu = f"Elegir opción:\nhttps://<url-destino>{salto + 'atras' if boton_atras else ''}{salto + 'adelante' if boton_adelante else ''}\nsalir\n  ==> "
        opcion = input(menu).lower()
        if opcion == "salir":
            pila_atras.clear()
            pila_adelante.clear()
            print("Navegador cerrado.")
            break
        pagina = navegar(opcion)

        print(f"\nEstoy en página https://{pagina}\n")
        habilitar_botones()


@anonymous_block
def dificultad_extra_imprimir():
    class PrintSpooler(LinearStructure):
        def __init__(self, tipo):
            super().__init__(tipo)
            if not self.validate():
                raise TypeError(f"Solo puede instanciar COLA.")

        def print_doc(self) -> None:
            print(f"Printing {self.take()}")

        def print_all(self) -> None:
            while self.elementos:
                self.print_doc()

        def remove_doc(self, doc_idx: int):
            if doc_idx == 0:
                print(f"Doc {self.elementos[0]} is Ready To Print => can't be removed.")
            else:
                print(f"Removig {self.elementos.pop(doc_idx)}")

        def list_spool(self):
            if not self.elementos:
                print("Spooler vacío.")
            else:
                for index, doc in enumerate(self.elementos):
                    if index == 0:
                        print(f"Document {doc} is ready to print.")
                    else:
                        print(f"Document {doc} is waiting for ({index}) document to print.")

        def validate(self):
            return self.tipo == "COLA"

    spooler = PrintSpooler("COLA")

    menu = f"""
    Menu de impresora:
        Documento (nombre)
        Eliminar
        Imprimir
        ImprimirTodo
        Listar
        Salir
    opcion => """

    while True:
        opcion = input(menu)
        if opcion.lower() == "salir":
            spooler.clear()
            print("\n\nSaliendo.")
            break
        if opcion.lower() == "imprimir":
            spooler.print_doc()
        elif opcion.lower() == "imprimirtodo":
            spooler.print_all()
        elif opcion.lower() == "listar":
            spooler.list_spool()
        elif opcion.lower() == "eliminar":
            if spooler:
                spooler.list_spool()
                doc_id = "-1"
                while not doc_id.isnumeric() or int(doc_id) not in range(0, spooler.__len__()):
                    doc_id = input("\nIngrese el número de orden del documento a eliminar: ")
                spooler.remove_doc(int(doc_id))
            else:
                print("No hay elementos en el spooler.")
        else:
            print(f"Mando a imprimir {opcion}", end="\n\n")
            spooler.put(opcion)

    print(f"{spooler} => Spool vacío. FIN del procesamiento.")
