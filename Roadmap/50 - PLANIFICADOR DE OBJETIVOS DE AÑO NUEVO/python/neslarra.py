r"""
 EJERCICIO:
 El nuevo año está a punto de comenzar...
 ¡Voy a ayudarte a planificar tus propósitos de nuevo año!

 Programa un gestor de objetivos con las siguientes características:
 - Permite añadir objetivos (máximo 10)
 - Calcular el plan detallado
 - Guardar la planificación
 
 Cada entrada de un objetivo está formado por (con un ejemplo):
 - Meta: Leer libros
 - Cantidad: 12
 - Unidades: libros
 - Plazo (en meses): 12 (máximo 12)

 El cálculo del plan detallado generará la siguiente salida:
 - Un apartado para cada mes
 - Un listado de objetivos calculados a cumplir en cada mes
   (ejemplo: si quiero leer 12 libros, dará como resultado 
   uno al mes)
 - Cada objetivo debe poseer su nombre, la cantidad de
   unidades a completar en cada mes y su total. Por ejemplo:

   Enero:
   [ ] 1. Leer libros (1 libro/mes). Total: 12.
   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
   Febrero:
   [ ] 1. Leer libros (1 libro/mes). Total: 12.
   ...
   Diciembre:
   [ ] 1. Leer libros (1 libro/mes). Total: 12.

 - Si la duración es menor a un año, finalizará en el mes
   correspondiente.
   
 Por último, el cálculo detallado debe poder exportarse a .txt
 (No subir el fichero)
"""


class Target:
    target_list = []

    def __new__(cls, target: str, target_unit: str, amount: int = 1, period: int = 12):
        if cls.number_of_targets() >= 10:
            raise "No se puede agregar más objetivos (10/10 máximo alcanzado)."
        if not (target and target_unit):
            raise "Debe indicar un objetivo específico y la unidad en la que se evaluará el avace."
        if not (0 < period < 13):
            raise "El período debe estar entr 1 y 12 meses."
        instance = super().__new__(cls)
        cls.target_list.append(instance)
        return instance

    def __init__(self, target: str, target_unit: str, amount: int = 1, period: int = 12):
        self.target = target
        self.target_unit = target_unit
        self.amount = amount
        self.period = period

    @classmethod
    def number_of_targets(cls):
        return cls.target_list.__len__()

    def __str__(self):
        return f"Objetivo: {self.target}\n\tPeríodo: {self.period}\n\tCantidad: {self.amount}\n\tUnidades: {self.target_unit}"

    def get_target(self):
        return self.target

    def get_target_unit(self):
        return self.target_unit

    def get_amount(self):
        return self.amount

    def get_period(self):
        return self.period


class TargetManager:
    def __init__(self, target_list: list[Target]):
        self.target_list = target_list

    def show_monthy_targets(self):
        months = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
                  7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
        print("\nObjetivos para este año ----------------")
        for target in self.target_list:
            print(f"{target.__str__()}")
        for month in range(1, 13):
            print(f"\nObjetivos {months[month]}\n{'#' * 30}")
            for target in self.target_list:
                monthly_activity = (target.get_amount() / target.get_period()).__round__(2)
                if target.get_amount() <= target.get_period():
                    if target.get_amount() >= month:
                        print(f"\t{target.get_target()}: 1 {target.get_target_unit()}")
                        continue
                if target.get_amount() > target.get_period():
                    if month <= target.get_period():
                        print(f"\t{target.get_target()}: {monthly_activity} {target.get_target_unit()}")
                        continue
                if monthly_activity > 1 and target.get_period() >= month:
                    print(f"\t{target.get_target()}: {monthly_activity} {target.get_target_unit()}")


objetivo1 = Target("Leer", "libros", 7, 12)
objetivo2 = Target("Ver", "videos", 12, 12)
objetivo3 = Target("Escribir", "Artículos", 17, 9)

gestor = TargetManager(Target.target_list)

gestor.show_monthy_targets()

objetivo4 = Target("Tomar", "Clases de tenis", 24, 6)

gestor.show_monthy_targets()
