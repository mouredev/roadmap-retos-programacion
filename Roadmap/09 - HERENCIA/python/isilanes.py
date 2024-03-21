import random
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    We make this class abstract, because we decided that no entity in our code
    can be just "an animal". It must be SOME animal, of some species (subclass).
    """

    def __init__(self, name: str):
        self.name = name
        self.food: int = 0  # amount of food inside the animal

    def eat(self, food: int = 1) -> None:
        self.food += food

    def poo(self) -> None:
        self.food -= 1

    @abstractmethod
    def make_noise(self) -> None:
        """
        Execute whatever sound the animal makes.
        """


class Perro(Animal):

    @staticmethod
    def bark() -> None:
        print("Guau!")

    def poo(self) -> None:
        """
        Dogs are renowned for how much they shit. Therefore, we override the default method.
        """
        self.food -= 2

    def make_noise(self) -> None:
        self.bark()


class Gato(Animal):

    @staticmethod
    def meow() -> None:
        print("Miauuuu")

    def make_noise(self) -> None:
        self.meow()


class Employee:
    """
    Esta vez no hacemos 'Empleado' abstracta, porque digamos que hemos decidido que podrían
    existir empleados que no tienen un tipo concreto. La típica gente que no sabes qué hace.
    """
    def __init__(self, name: str, employee_id: int, minions: list['Employee'] | None = None):
        self.name = name

        # Esta implementación de ID de empleado debería enviarme directamente a la cárcel.
        # Obviamente hay dos requisitos que deberían considerarse mínimos, y que esta
        # implementación no cumple:
        # - Debería poder asignarse un ID de manera automática, sin pasarlo como argumento
        # - Debería garantizarse que los IDs son únicos.
        # Ambos requisitos suelen ser estándar en implementaciones apoyadas en base de datos,
        # como los modelos en Django (se transfiere la responsabilidad de ello a la db).
        # Sin base de datos, podríamos implementarlo con UUIDs, o con algún repositorio
        # central de IDs.
        self.employee_id = employee_id

        # El enunciado parece sugerir que implementemos la relación one-to-many de manera inversa
        # a como se haría en una base de datos. En vez de definir un atributo 'dependo de' en
        # el subalterno, que apunte a su jefe (de forma que "los subalternos de X" son "los elementos
        # cuyo 'dependo de' apunta a X"), definimos un atributo ' dependen de mí' en el jefe,
        # que contiene a los subalternos de ese elemento (de manera que "los subaltennos de X" son
        # directamente "los elementos en la lista 'dependen de mí' de X"). Va más allá del alcance de
        # este ejercicio discutir los méritos de ambas aproximaciones, y por qué la otra es mejor que esta :)
        self.minions = minions or []


class Engineer(Employee):
    """
    Los programadores, los IndividualContributors, los machacas, los curritos. Los verdaderos héroes sin capa :D
    """

    def __init__(self, name: str, employee_id: int):
        super().__init__(name=name, employee_id=employee_id)  # los curritos no tienen minions

    @staticmethod
    def produce_spaghetti() -> None:
        print("Marchándo una de código infumable...")

    @staticmethod
    def guess_deadline() -> float:
        return random.randrange(1, 1000)


class ProjectManager(Employee):
    """
    Los Gerentes de Proyecto, o PMs. Los jefes intermedios que te venden que no son jefes intermedios,
    sino engranajes de tu proyecto ágil al mismo nivel que el resto de miembros, pero que vamos,
    que son jefes intermedios.
    """
    def __init__(self, name: str, employee_id: int, minions: list[Engineer] | None = None):
        super().__init__(name=name, employee_id=employee_id, minions=minions)

    def ask_for_estimations(self, feature: str) -> None:
        if not self.minions:
            print(f"No tengo programadores a mi cargo, no puedo hacer {feature}")
            return

        print(f"{self.name}: Chic@s, decidme cuánto creéis que se tarda en implementar {feature}")
        for minion in self.minions:
            print(f"{minion.name}: yo creo que {minion.guess_deadline()} días.")


class CEO(Employee):
    """
    El Gerente, el jefe, el boss. El CEO es jefe directo de todos los PMs (Gerentes de Proyecto).
    """
    def __init__(self, name: str, minions: list[ProjectManager] | None = None):
        super().__init__(name=name, employee_id=0, minions=minions)  # el CEO tiene el ID primigenio

        self.n_yachts = 1

    def park(self) -> None:
        print(f"El jefe {self.name} aparca donde le da la gana.")

    def sail(self) -> None:
        if self.n_yachts > 1:
            print(f"El jefe {self.name} navega en uno de sus {self.n_yachts} yates.")
        elif self.n_yachts == 1:
            print(f"El jefe {self.name} navega en su yate.")
        else:
            print("Nos compramos un yate...")
            self.n_yachts += 1
            self.sail()

    def request_feature(self, feature: str) -> None:
        for pm in self.minions:
            print(f"{self.name}: Oye, {pm.name}, hacedme {feature}")
            pm.ask_for_estimations(feature)


def main():
    print("Nuestras clases Perro y Gato heredan de la clase (abstracta) Animal. No puedo instanciar un Animal abstracto:")
    print('yo = Animal(name="Iñaki")')
    try:
        yo = Animal(name="Iñaki")
    except TypeError:
        print("Te dije que no se puede.")

    print("\nSí que podemos instanciar un Gato:")
    print('cat = Gato(name="Félix")')
    cat = Gato(name="Félix")
    print("El gato puede maullar:")
    print('cat.meow()')
    cat.meow()
    print("Como todas las subclases de Animal, un Gato tiene el método make_noise(), que en su caso maullará:")
    print('cat.make_noise()')
    cat.make_noise()
    print("El Gato, como todos los Animales, tiene un nombre, y una cantidad de comida en su estómago:")
    print(f"cat.name == {cat.name}, cat.food == {cat.food}")
    print("Un Gato puede comer una cantidad arbitraria de unidades de comida:")
    print('cat.eat(3)')
    cat.eat(3)
    print("Ahora tendrá más comida dentro:")
    print(f"cat.food == {cat.food}")
    print("(No se me escapa que mi chapucera implementación de eat() permite aberraciones,")
    print("como por ejemplo comer una cantidad negativa de comida)")
    print("Un gato puede también cagar, lo cual en su caso hace con la cantidad estándar de 1 unidad de comida:")
    print('cat.poo()')
    cat.poo()
    print(f"cat.name == {cat.name}, cat.food == {cat.food}")

    print("\nTambién podemos instanciar un Perro, el cual tiene nombre y cantidad de comida ingerida,")
    print("como el Gato:")
    print('dog = Perro("Pluto")')
    dog = Perro("Pluto")
    print(f"dog.name == {dog.name}, dog.food == {dog.food}")
    print("Un Perro puede ladrar (bark), y también puede hacer un sonido (make_noise), lo cual,")
    print("en su caso, corresponde a ladrar:")
    print('dog.bark()')
    dog.bark()
    print('dog.make_noise()')
    dog.make_noise()
    print("Un Perro también puede comer y cagar, como cualquier Animal. En su caso, caga más:")
    print('dog.eat(3)')
    dog.eat(3)
    print(f"dog.name == {dog.name}, dog.food == {dog.food}")
    print('dog.poo()')
    dog.poo()
    print(f"dog.name == {dog.name}, dog.food == {dog.food}")

    print("\nEl 'duck typing' de Python, unido al uso de una superclase abstracta en este caso,")
    print("nos permite recorrer una colección de Animales, y hacer que cada uno haga 'su sonido',")
    print("usando el método make_noise() que sabemos que tienen, y sin preocuparnos de qué")
    print("subclase concreta de Animal son:")
    for animal in (dog, cat):
        print(f"El {animal.__class__.__name__} {animal.name} hace...")
        animal.make_noise()


def extra():
    print("\nTenemos una empresa, en la que alguien puede ser un empleado sin oficio ni beneficio:")
    print('nobody = Employee(name="Santiago", employee_id=1)')
    nobody = Employee(name="Santiago", employee_id=1)

    print("\nMás interesantes son los programadores, sustento de la empresa y maravillosos seres de luz:")
    print('alice = Engineer(name="Alice", employee_id=2)')
    print('bob = Engineer(name="Robert", employee_id=3)')
    print('charlie = Engineer(name="Charles", employee_id=4)')
    alice = Engineer(name="Alice", employee_id=2)
    bob = Engineer(name="Bob", employee_id=3)
    charlie = Engineer(name="Charlie", employee_id=4)
    print("Un programador puede producir bas... código:")
    print('alice.produce_spaghetti()')
    alice.produce_spaghetti()
    print("Todo programador que se precie puede generar estimaciones:")
    print(f"bob.guess_deadline() == {bob.guess_deadline()}")
    print(f"charlie.guess_deadline() == {charlie.guess_deadline()}")
    print(f"charlie.guess_deadline() == {charlie.guess_deadline()}")
    print("(No dijimos que fueran a ser consistentes)")

    print("\nUn buen proyecto tendrá un PM, que se encargará de varios Programadores:")
    print('michael = ProjectManager(name="Scott", employee_id=5, minions=[alice, bob, charlie])')
    michael = ProjectManager(name="Scott", employee_id=5, minions=[alice, bob, charlie])
    print("La principal función de un PM es pedir estimaciones:")
    print('michael.ask_for_estimations(feature="un botón bonito")')
    michael.ask_for_estimations(feature="un botón bonito")
    print("Es posible que un PM no tenga empleados a su cargo:")
    print('andy = ProjectManager(name="Bernard", employee_id=6)')
    andy = ProjectManager(name="Bernard", employee_id=6)
    print(f"{andy.name} tiene estos subalternos: {andy.minions}")

    print("\nFinalmente llegamos al Gerente/CEO/jefe. Este tendrá PMs a su cargo:")
    print('boss = CEO(name="Bruce S.", minions=[michael, andy])')
    boss = CEO(name="Bruce S.", minions=[michael, andy])
    print("Un buen CEO puede hacer cosas chachis:")
    print('boss.park()')
    boss.park()
    print('boss.sail()')
    boss.sail()
    print("Y si no tenemos yate...")
    print('boss.n_yachts = 0')
    boss.n_yachts = 0
    print('boss.sail()')
    boss.sail()
    print("""boss.request_feature("una web 'como la de Iberia'")""")
    boss.request_feature("una web 'como la de Iberia'")


if __name__ == "__main__":
    main()
    extra()
