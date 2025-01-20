# /*
#  * EJERCICIO:
#  * El nuevo año está a punto de comenzar...
#  * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
#  *
#  * Programa un gestor de objetivos con las siguientes características:
#  * - Permite añadir objetivos (máximo 10)
#  * - Calcular el plan detallado
#  * - Guardar la planificación
#  * 
#  * Cada entrada de un objetivo está formado por (con un ejemplo):
#  * - Meta: Leer libros
#  * - Cantidad: 12
#  * - Unidades: libros
#  * - Plazo (en meses): 12 (máximo 12)
#  *
#  * El cálculo del plan detallado generará la siguiente salida:
#  * - Un apartado para cada mes
#  * - Un listado de objetivos calculados a cumplir en cada mes
#  *   (ejemplo: si quiero leer 12 libros, dará como resultado 
#  *   uno al mes)
#  * - Cada objetivo debe poseer su nombre, la cantidad de
#  *   unidades a completar en cada mes y su total. Por ejemplo:
#  *
#  *   Enero:
#  *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
#  *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
#  *   Febrero:
#  *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
#  *   ...
#  *   Diciembre:
#  *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
#  *
#  * - Si la duración es menor a un año, finalizará en el mes
#  *   correspondiente.
#  *   
#  * Por último, el cálculo detallado debe poder exportarse a .txt
#  * (No subir el fichero)
#  */
import math
import os

class Gestor:
    __LIMIT = 10 # Máximo de objetivos permitidos por usuario, restaremos cada vez que se añada un objetivo.
    __LIMIT_MONTHS = 12 # Máximo de meses permitidos para el plazo de un objetivo.
    __MONTHS = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    __PROCECED_DATA = [] # Datos procesados para poder guardarlos en un archivo además de mostrarlos en consola.

    def __init__(self):
        self.objetivos = [] # Lista de objetivos
        self.__LIMIT_MONTHS = 12

    def calcular(self):
        """
        Calcula los objetivos mensuales y los estructura para cada mes.
        en los objetivos que tengan plazo impar, se redondeará hacia arriba para no tener decimales.
        """
        self.__PROCECED_DATA = []  # Limpieza de datos procesados

        # Recorremos los objetivos para calcular su distribución mensual
        for objetivo in self.objetivos:
            # Obtenemos los datos del objetivo
            cantidad = objetivo['cantidad']  # Total de unidades
            plazo = objetivo['plazo']  # Meses disponibles
            meta = objetivo['meta']  # Descripción del objetivo
            unidad = objetivo['unidad']  # Unidad del objetivo

            restante = cantidad  # Inicializamos el restante
            cuota_mensual = cantidad / plazo  # Cálculo de cuota base por mes

            for mes in range(plazo):
                cantidad_mes = max(math.ceil(cuota_mensual),1)  # Cuota redondeada minimizando a 1
                if restante < cantidad_mes:
                    cantidad_mes = restante  # Ajustamos la cuota al restante

                restante -= cantidad_mes  # Reducimos el restante
                nuevo_objetivo = {
                    'mes': self.__MONTHS[mes],  # Mes correspondiente
                    'meta': meta,  # Meta del objetivo
                    'cantidad': cantidad_mes,  # Cantidad para el mes
                    'unidad': unidad,  # Unidad asociada
                    'total': cantidad,  # Total del objetivo
                }
                if cantidad_mes > 0:
                    self.__PROCECED_DATA.append(nuevo_objetivo)  # Añadimos al resultado

        self.mostrar_objetivos()  # Muestra los objetivos procesados


    def limpiar_fichero(self):
        """
        Limpia el archivo de texto donde se guardan los objetivos
        """
        file_ruta = self.obtener_fichero()
        with open(file_ruta, 'w', encoding="utf-8") as file:
            file.write('')

    def obtener_fichero(self):
        """
        Obtiene el archivo de texto donde se guardan los objetivos
        """
        return os.path.join(os.getcwd(), 'objetivos.txt')
    
    def guardar(self):
        """
        Guarda los objetivos procesados en un archivo de texto
        """
        #limpiamos el archivo de texto
        self.limpiar_fichero()
        #obtenemos la ruta del archivo de texto
        file_ruta = self.obtener_fichero()

        objetivos_por_mes = {}

        # Agrupamos los objetivos por mes

        for objetivo in self.__PROCECED_DATA:
            # Obtenemos el mes del objetivo
            mes = objetivo['mes']
            # Si el mes no está en el diccionario, lo añadimos
            if mes not in objetivos_por_mes:
                # Inicializamos la lista de objetivos
                objetivos_por_mes[mes] = []
            # Añadimos el objetivo a la lista correspondiente
            objetivos_por_mes[mes].append(objetivo)

            # Abrimos el archivo de texto y sobre escribimos mes a mes
            with open(file_ruta, 'r+', encoding="utf-8") as file:
                for mes, objetivos in objetivos_por_mes.items():
                    # Mostramos el mes
                    file.write(f'{mes}:\n')
                    # Mostramos los objetivos del mes
                    for i, objetivo in enumerate(objetivos):
                        #escribimos en el archivo de texto con el objetivo
                        file.write(f'[{i+1}] {objetivo["meta"]} ({objetivo["cantidad"]} {objetivo["unidad"]}/mes). Total: {objetivo["total"]}.\n')
                    #saltamos una linea
                    file.write('\n')
            #cerramos el archivo de texto
            file.close()    

    def add_objetivo(self,meta: str, cantidad:int, unidad:str, plazo:int)->None:
        """
        Añade un objetivo a la lista de objetivos.
        - Meta: Leer libros
        - Cantidad: 12
        - Unidades: libros
        - Plazo (en meses): 12 (máximo 12)
        """
        # Validaciones
        if(self.__LIMIT == 0):
            print('Has alcanzado el máximo de objetivos permitidos.')
            return
        
        if(plazo > self.__LIMIT_MONTHS):
            print(f'El plazo no puede ser mayor a {self.__LIMIT_MONTHS} meses.')
            return
        
        if cantidad <= 0:
            print('La cantidad no puede ser menor o igual a 0.')
            return
        
        # añadir objetivo cuando se cumplan las validaciones.
        self.objetivos.append({
            'meta': meta,
            'cantidad': cantidad,
            'unidad': unidad,
            'plazo': plazo
        })
        self.__LIMIT -= 1
        print(f'Objetivo añadido: {meta}')
        


    def mostrar_objetivos(self):
        """
        Muestra los objetivos procesados por mes en el formato requerido.
        """
        if not self.__PROCECED_DATA:
            print("No hay objetivos procesados.")
            return

        objetivos_por_mes = {}
        # Agrupamos los objetivos por mes
        for objetivo in self.__PROCECED_DATA:
            # Obtenemos el mes del objetivo
            mes = objetivo['mes']
            # Si el mes no está en el diccionario, lo añadimos
            if mes not in objetivos_por_mes:
                # Inicializamos la lista de objetivos
                objetivos_por_mes[mes] = []
            # Añadimos el objetivo a la lista correspondiente
            objetivos_por_mes[mes].append(objetivo)
        for mes, objetivos in objetivos_por_mes.items():
            # Mostramos el mes
            print(f'{mes}:')
            # Mostramos los objetivos del mes
            for i, objetivo in enumerate(objetivos):
                print(f'[{i+1}] {objetivo["meta"]} ({objetivo["cantidad"]} {objetivo["unidad"]}/mes). Total: {objetivo["total"]}.')
            print()


if __name__ == '__main__':
    gestor = Gestor()
    # Añadimos los objetivos al gestor.

    gestor.add_objetivo('Leer libros', 12, 'libros', 12)
    gestor.add_objetivo('Estudiar Git', 1, 'curso', 1)
    gestor.add_objetivo('Hacer ejercicio', 12, 'rutina', 12)
    gestor.add_objetivo('Aprender Python', 12, 'curso', 7)
    gestor.add_objetivo('Aprender Javascript', 7, 'curso', 12)
    gestor.add_objetivo('Aprender Vue', 8, 'curso', 9)
    gestor.add_objetivo('Aprender Svelte', 12, 'curso', 4)
    gestor.add_objetivo('Aprender React', 10, 'curso', 4)
    gestor.add_objetivo('Aprender Angular', 2, 'curso', 4)
    gestor.add_objetivo('Aprender Node', 8, 'curso', 4)

    gestor.calcular()
    gestor.guardar()