import uuid


# Superclase animal y subclases perro y gato
class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound_of_animal(self):
        pass


class Dog(Animal):
    def sound_of_animal(self):
        return print("Guau Guau")


class Cat(Animal):
    def sound_of_animal(self):
        return print("Miau Miau")


# Extra
# Jerarquía
class Employees:
    employees_subordinates = []

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def add_subordinate(self, id, name, boss):
        self.employees_subordinates.append({"id": id, "name": name, "boss": boss})

    def subordinates(self, boss):
        subordinates_list = [
            element
            for element in self.employees_subordinates
            if element["boss"] == boss
        ]
        return print(subordinates_list)


class Managers(Employees):
    def organize(self):
        print("El Gerente esta organizando una junta...")

    def hire(self):
        print("El Gerente esta contratando personal")

    def to_plan(self):
        print("El Gerente esta planificando una estrategía para obtener más clientes")


class ProjectManagers(Employees):
    def lead(self):
        print("El Gerente de Proyecto esta dirigiendo al equipo de desarrollo")

    def define_objectives(self):
        print(
            "El Gerente de Proyecto esta definiendo los objetivos para el backend del proyecto"
        )

    def to_motivate(self):
        print("El Gerente de Proyecto esta motivando a los desarrolladores")


class Developers(Employees):
    technological_stack = []

    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def program(self):
        print("El pogramador esta programando en su lenguaje favorito")

    def add_technology(self, technology):
        self.technological_stack.append(technology)

    def get_technological_stack(self):
        print(self.technological_stack)

    def role(self):
        print(f"El programador es: {self.role}")


if __name__ == "__main__":
    dog = Dog(name="Boby", breed="Pastor aleman")
    dog.sound_of_animal()
    cat = Cat(name="Mishi", breed="Siames")
    cat.sound_of_animal()

    manager = Managers("Raul Jimenez")
    project_manager1 = ProjectManagers("Saul Najera")
    project_manager2 = ProjectManagers("Leticia Olmedo")
    backend_1 = Developers("Miguel Angel López", "Desarrollador Backend")
    backend_2 = Developers("Romina Palafox", "Desarrollador Backend")
    backend_3 = Developers("Alma Benavides", "Desarrollador Backend")
    frontend_1 = Developers("Luis Mendoza", "Desarrollador Frontend")
    frontend_2 = Developers("Ramiro Gutierrez", "Desarrollador Frontend")
    frontend_3 = Developers("Stefania Riquelme", "Desarrollador Frontend")
    devops_1 = Developers("Ramiro Corona", "Devops")
    devops_2 = Developers("Reina Camacho", "Devops")

    manager.add_subordinate(project_manager1.id, project_manager1.name, boss=manager.id)
    manager.add_subordinate(project_manager2.id, project_manager2.name, boss=manager.id)
    print(f"Los subordinados del Gerente {manager.name} son: ")
    manager.subordinates(manager.id)
    project_manager1.add_subordinate(
        backend_3.id,
        backend_3.name,
        boss=project_manager1.id,
    )
    project_manager1.add_subordinate(
        frontend_1.id,
        frontend_1.name,
        boss=project_manager1.id,
    )
    project_manager1.add_subordinate(
        frontend_2.id,
        frontend_2.name,
        boss=project_manager1.id,
    )
    project_manager1.add_subordinate(
        devops_1.id,
        devops_1.name,
        boss=project_manager1.id,
    )
    print(f"Los subordinados del Gerente de Proyecto 1 {project_manager1.name} son: ")
    project_manager1.subordinates(project_manager1.id)
    project_manager2.add_subordinate(
        backend_1.id,
        backend_1.name,
        boss=project_manager2.id,
    )
    project_manager2.add_subordinate(
        backend_2.id,
        backend_2.name,
        boss=project_manager2.id,
    )
    project_manager2.add_subordinate(
        frontend_3.id,
        frontend_3.name,
        boss=project_manager2.id,
    )
    project_manager2.add_subordinate(
        devops_2.id,
        devops_2.name,
        boss=project_manager2.id,
    )
    print(f"Los subordinados del Gerente de Proyecto 2 {project_manager2.name} son: ")
    project_manager2.subordinates(project_manager2.id)
