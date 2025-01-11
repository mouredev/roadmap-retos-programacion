"""
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 *
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
"""
import os


class Planificador:

    def __init__(self):
        self.objetivos = {}
        self.planificacion = []

    def agregar_objetivos(self, numero_objetivos):
        contador = 1

        while 11 > numero_objetivos > 0:

            numero_objetivos -= 1
            print(f"""\n| Ingresando el objetivo {
                  contador} |""", end=f'\n{"¯"*28}')

            meta = input('\n\t• Ingresa la meta: ')

            try:
                cantidad = int(input('\n\t• Ingresa la cantidad: '))
            except ValueError:
                print('\nIngresa sólo números\n')

            unidades = input('\n\t• Ingresa las unidades: ')

            try:
                plazo = int(
                    input('\n\t• Ingresa el plazo(en meses y máximo 12): '))
            except ValueError:
                print('\nIngresa sólo números\n')

            if plazo > 12:
                print(
                    '\nNo puedes ingresar más de 12 meses, ingresa todos los datos nuevamente\n')
                numero_objetivos += 1

            else:
                self.objetivos.update(
                    {f"objetivo{contador}": {"Meta": meta,
                                             "Cantidad": cantidad,
                                             "Unidades": unidades,
                                             "Plazo": plazo}
                     })
                contador += 1

    def calcular_plan(self):
        """
        Calcula el plan de objetivos y los muestra en la terminal
        """
        if self.objetivos:
            objetivos = [objetivo[1] for objetivo in self.objetivos.items()]
            mes_plazo = [objetivo[1]['Plazo']
                         for objetivo in self.objetivos.items()]

            max_mes = max(mes_plazo)

            meses = ["Enero",
                     "Febrero",
                     "Marzo",
                     "Abril",
                     "Mayo",
                     "Junio",
                     "Julio",
                     "Agosto",
                     "Septiembre",
                     "Octubre",
                     "Noviembre",
                     "Diciembre"
                     ]

            for valor_mes in range(0, max_mes):

                mes = meses[valor_mes]
                self.planificacion.append([mes])

                print(f'\n\n{mes} {"—"*(11 - len(mes))}|{"—"*60}\n')

                for ciclo, dato in enumerate(objetivos, 1):

                    if dato['Plazo'] >= (valor_mes + 1):

                        cantidad_mensual = dato['Cantidad'] / \
                            dato['Plazo'] if dato['Cantidad'] > 1 else dato['Cantidad']

                        cantidad_total = f'{dato['Plazo']} {
                            "Meses" if dato['Plazo'] > 1 else "Mes"}'

                        objetivo_mes = f'[ ] {ciclo}. {dato['Meta']} ({cantidad_mensual} {
                            dato['Unidades']}/mes). Cantidad total: {cantidad_total}'

                        self.planificacion[valor_mes].append(objetivo_mes)

                        print(f'{" "*12}{objetivo_mes}')
        else:
            print(
                '\n\tDebes agregar los objetivos para realizar el calculo del plan detallado\n')

    def exportar_planificacion(self):
        """
        Acá se guarda el archivo en plan_detallado.txt con
        el contenido de los objetivos
        """
        if self.planificacion:
            nombre_archivo = "plan_detallado.txt"
            ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)

            with open(ruta, "w", encoding="utf-8") as archivo:
                print('\n\tComenzado la exportación del archivo')

                archivo.write('\t\t\tPlanificación de objetivos\n')
                for mes_planificado in self.planificacion:
                    for planificacion in mes_planificado:

                        if mes_planificado[0] == planificacion:
                            archivo.write(f"""\n\n{planificacion} {
                                "—"*(11 - len(planificacion))}|{"—"*60}\n""")
                        else:
                            archivo.write(f'\n{" "*12}{planificacion}')

                print(f'\n\tSe realizo con exito la exportación del plan detallado, busca el archivo: {
                    nombre_archivo}')
        else:
            print(
                '\n\tPara exportar, primero debes realizar el calculo de la planificación\n')


def cantidad_objetivos(ciclo):

    while ciclo:

        try:
            objetivos = input(
                '\n• Ingresa la cantidad de Objetivos(Máximo 10): ')

        except ValueError:
            print('\nSolo puedes ingresar números\n')

        if objetivos.isdigit():
            n_objetivo = int(objetivos)

            if n_objetivo > 10:
                print('\nRecuerda solo puedes ingresar 10 objetivos\n')

            elif n_objetivo < 0:
                print('\nNo puedes ingresar números negativos\n')
            else:
                ciclo = False
                return n_objetivo


def menu():

    opciones = [
        "1. Ingresar objetivo",
        "2. Calcular la planificación",
        "3. Exportar la planifición a un archivo .txt",
        "4. Salir"
    ]

    print('\n\n\tPlanificado de objetivos de año nuevo\n')
    for opcion in opciones:
        print(f'\t{opcion}')

    try:
        n_opcion = int(input('\nIngresa una opción del menu: '))

    except ValueError:
        n_opcion = '_'

    return n_opcion


def main():

    plan = Planificador()

    print('\n\tBienvenidos al Gestor de Objetivos del año nuevo')

    while True:
        n_opcion = menu()

        match n_opcion:
            case 1:
                c_objetivo = cantidad_objetivos(True)
                plan.agregar_objetivos(c_objetivo)
            case 2:
                plan.calcular_plan()
            case 3:
                plan.exportar_planificacion()
            case 4:
                break
            case _:
                print('\n\tError, Opción no encontrada, ingresa sólo números del menú\n')


if __name__ == '__main__':
    main()
