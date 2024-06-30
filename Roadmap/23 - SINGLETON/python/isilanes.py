class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class Patata(metaclass=SingletonMeta):

    def __init__(self, size: int = 10, color: str = "yellow") -> None:
        self.size = size
        self.color = color

    def __str__(self) -> str:
        return f"Patata(s={self.size}, c='{self.color}')"


def main():
    print("===== MAIN =====")
    print("Creamos un objeto de la clase Patata")
    print('>>> p1 = Patata()')
    p1 = Patata()
    print(f"p1 == {p1}")
    print("Intentamos crear una segunda Patata, inicializada con valores diferentes:")
    print('>>> p2 = Patata(size=20, color="red")')
    p2 = Patata(size=20, color="red")
    print("Sin embargo, p2 es idéntica a p1:")
    print(f"p2 == {p2}")
    print("Esto es porque Patata es una clase singleton, y por tanto p2 no se ha instanciado, sino tomado de p1:")
    print(">>> p1 is p2")
    print(p1 is p2)
    print("Cambiar un atributo de cualquiera de los dos objetos lo cambia en ambos:")
    print('p1.size = 100')
    p1.size = 100
    print(f"p2 == {p2}")
    print('>>> p2.color = "green"')
    p2.color = "green"
    print(f"p1 == {p1}")


if __name__ == "__main__":
    main()
