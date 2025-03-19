"""
 EJERCICIO:
 Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 implemente una superclase Animal y un par de subclases Perro y Gato,
 junto con una función que sirva para imprimir el sonido que emite cada Animal.

 DIFICULTAD EXTRA (opcional):
 Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 Cada empleado tiene un identificador y un nombre.
 Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 actividad, y almacenan los empleados a su cargo.
"""


class Animal:
    mascotas = 0

    def __init__(self, patas: int, sonido: str, tipo_piel: str, movilidad: str):
        self.patas = patas
        self.sonido = sonido
        self.tipo_piel = tipo_piel
        self.movilidad = movilidad
        self.validar()
        Animal.alta_mascota()

    def validar(self):
        if not (0 <= self.patas <= 4) or (self.patas % 2 > 0):
            raise AttributeError("Error: Cantidad de patas NO corresponde.")
        if self.tipo_piel.lower() not in ("pelaje", "plumas", "escamas"):
            raise AttributeError("Error: Tipo de piel desconocida.")
        if self.movilidad.lower() not in ("camina", "repta", "vuela", "nada"):
            raise AttributeError("Error: Tipo de movilidad no corresponde.")

    def comunicacion(self):
        return f"Este tipo de animal emite un {self.sonido}."

    def __str__(self):
        if self.patas == 4:
            detalle = f"en {self.patas} patas."
        elif self.patas == 2:
            detalle = f"con {self.patas} alas."
        elif self.movilidad == "nada":
            detalle = f"con una aleta caudal, dos pectorales y una (o más) dorsal."
        elif self.movilidad == "repta":
            detalle = f"con una musculatura adaptada en su parte ventral."
        else:
            detalle = "movildad a evaluar."
        return f"{self.movilidad.capitalize()} {detalle} {self.comunicacion()}"

    @classmethod
    def alta_mascota(cls):
        cls.mascotas += 1


class Perro(Animal):
    mascotas = 0

    def __init__(self, nombre: str, raza: str, color: str):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        Perro.alta_mascota()
        super().__init__(4, "ladrido", "pelaje", "camina")

    def __str__(self):
        return f"{self.nombre.capitalize()} es un perro de raza {self.raza.lower()} con {self.tipo_piel.lower() } de color {self.color.lower()}. {super().__str__()}"

    @classmethod
    def add_mascota(cls):
        cls.mascotas += 1


class Gato(Animal):
    mascotas = 0

    def __init__(self, nombre: str, raza: str, color: str):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        super().__init__(4, "maullido", "pelaje", "camina")
        Gato.alta_mascota()

    def __str__(self):
        return f"{self.nombre.capitalize()} es un gato de raza {self.raza.lower()} con {self.tipo_piel.lower() } de color {self.color.lower()}. {super().__str__()}"

    @classmethod
    def add_mascota(cls):
        cls.mascotas += 1


class Pajaro(Animal):
    mascotas = 0

    def __init__(self, especie: str, color: str):
        self.color = color
        self.especie = especie
        super().__init__(2, "vocalización", "plumas", "vuela")
        Pajaro.alta_mascota()

    @classmethod
    def add_mascota(cls):
        cls.mascotas += 1


class Pez(Animal):
    mascotas = 0

    def __init__(self, color: str, medio: str):
        self.color = color
        self.medio = medio
        super().__init__(0, "ninguno", "escamas", "nada")
        Pez.alta_mascota()

    def comunicacion(self):
        return f"Este tipo de animal NO emite ningún sonido."

    @classmethod
    def add_mascota(cls):
        cls.mascotas += 1


class Serpiente(Animal):
    mascotas = 0

    def __init__(self, color: str, veneno: str):
        self.color = color
        self.veneno = veneno
        super().__init__(0, "ninguno", "escamas", "repta")
        Serpiente.alta_mascota()

    def comunicacion(self):
        return f"Este tipo de animal NO emite ningún sonido."

    def peligrosidad(self):
        return f"Su veneno es potencialmente peligroso" if self.veneno.lower() == "si" else "NO representa peligro para las personas."

    @classmethod
    def add_mascota(cls):
        cls.mascotas += 1


print("""Cuando distintos objetos tienen algunos atributos en común y otros que los diferencian, se puede abstraer los atributos comunes en una
clase que luego los pasará a otras clases-hijas que los heredaran y aportarán sus propios atributos y métodos. También podrán modificar los métodos
heredados para adecuarlos a sus propias necesidades.
Creamos una Clase (madre) "Animal" de la cual heredarán las clases más particulares "Perro", "Gato", "Pájaro", "Pez" y "Serpiente" las cuales, a su
vez, agregarán sus propios atributos y métodos e incluso modificarán alguno de los heredados (ya sean de instancia o de clase). 
""")

luna = Perro("Luna", "Mestiza", "Blanco con parches negros")
thompson = Gato("Thompson", "Mestiza", "Negro con vetas blancas")
piopio = Pajaro("Canario", "Amarillo")
nemo = Pez("Naranja", "Agua salada")
viper = Serpiente("Dorado con diamantes marrones", "SI")
apolo = Perro("Apolo", "Daschund", "Negro")
aslan = Gato("Aslan", "Siamés", "beige")
rocky = Perro("Rocky", "Caniche Toy", "blanco")

print("La clase Animal es heredada por:", end=" ")
for clase in Animal.__subclasses__():
    print(f"{clase.__name__} con {clase.mascotas} instancias,", end=" ")
print(f"\nEn total heredan {Animal.mascotas} mascotas", end="\n\n")

for var in [luna, thompson, piopio, nemo, viper, apolo, aslan, rocky]:
    # print(f"Clase {var.__class__.__name__} hereda de {var.__class__.__base__.__name__}", end="\n\t")
    if var.__class__.__name__ == "Pez":
        print(f"Clase {var.__class__.__name__}. {var} Hereda de {var.__class__.__base__.__name__}. Se lo encuentra en {var.medio}")
    else:
        print(f"Clase {var.__class__.__name__}. {var} Hereda de {var.__class__.__base__.__name__}.")

# Dificultad Extra
print(f"\n{'#' * 50}\nDificultad Extra\n{'#' * 50}", end="\n\n")

"""
DIFICULTAD EXTRA (opcional):
 Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 Cada empleado tiene un identificador y un nombre.
 Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 actividad, y almacenan los empleados a su cargo.
"""


class Employee:
    emp = {}
    employes_ids = list(range(1000, 9999))

    def __init__(self, fullname: str, department: str, job: str, salary: int, project: str = "", main_skill: str = ""):
        self.fullname = fullname
        self.department = department
        self.job = job
        self.salary = salary
        self.employee_id = Employee.get_employee_id()
        Employee.add_employees(self.employee_id, self.fullname, self.department, self.job, self.salary, project, main_skill)

    def __str__(self):
        return f"Employee#: {self.employee_id} / Full Name: {self.fullname} / Department: {self.department} / Job: {self.job} / Salary: {self.salary}"

    @classmethod
    def get_employee_id(cls):
        return Employee.employes_ids.pop(0)

    @classmethod
    def add_employees(cls, employee_id, fullname, department, job, salary, project, main_skill):
        cls.emp[employee_id] = {"Fullname": fullname, "Department": department, "Job": job, "Salary": salary, "Project": project, "MainSkill": main_skill}


class Manager(Employee):
    def __init__(self, fullname: str, department: str):
        super().__init__(fullname, department, "Manager", 10000)

    def get_subordinates(self):
        subordinates = []
        for key, value in Employee.emp.items():
            if key != self.employee_id and Employee.emp[key]["Department"] == self.department:
                subordinates.append(Employee.emp[key]["Fullname"] + " / " + Employee.emp[key]["Job"])
        return subordinates


class ProjectManager(Employee):
    def __init__(self, fullname: str, department: str, project: str):
        self.project = project
        super().__init__(fullname, department, "Project Manager", 7000, project)

    def get_resources(self):
        resources = []
        for key, value in Employee.emp.items():
            if key != self.employee_id and Employee.emp[key]["Project"] == self.project:
                resources.append(Employee.emp[key]["Fullname"] + " / " + Employee.emp[key]["Job"] + " / " + Employee.emp[key]["MainSkill"])
        return resources


class Programmer(Employee):
    def __init__(self, fullname: str, department: str, project: str, main_skill: str):
        self.project = project
        self.main_skill = main_skill
        super().__init__(fullname, department, "Programmer", 5000, project, main_skill)


Tito = Manager("Tito Tulio", "IT")
Paco = ProjectManager("Paco Pega", "IT", "Banco Garca")
Pepe = Programmer("Pepe Botella", "IT", "Banco Garca", "C#")
Papo = Programmer("Papo Napo", "IT", "Banco Garca", "HTML5")

print(f"{Tito}\n\tDependants: {Tito.get_subordinates()}", end="\n\n")

print(f"{Paco}\n\tProject: {Paco.project}. Resources: {Paco.get_resources()}", end="\n\n")

print(f"{Pepe}\n\tMain Skill: {Pepe.main_skill} at project {Pepe.project}", end="\n\n")

print(f"{Papo}\n\tMain Skill: {Papo.main_skill} at project {Papo.project}", end="\n\n")
