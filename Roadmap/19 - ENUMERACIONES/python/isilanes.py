from enum import Enum


class Day(int, Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    @property
    def spanish_name(self) -> str:
        return {
            self.MONDAY: "lunes",
            self.TUESDAY: "martes",
            self.WEDNESDAY: "miércoles",
            self.THURSDAY: "jueves",
            self.FRIDAY: "viernes",
            self.SATURDAY: "sábado",
            self.SUNDAY: "domingo",
        }.get(self, "DESCONOCIDO")


def main(index: int):
    print(f"Al índice {index} le corresponde el siguiente objeto:")
    day = Day(index)
    print(f">>> day = Day({index})")
    print(f">>> str(day) == '{str(day)}'")
    print(f"El valor correspondiente es:")
    print(f">>> day.name == '{day.name}'")
    print("Para imprimir un valor 'humano' usaremos un método personalizado,")
    print("que deberemos haber implementado nosotros:")
    print(f">>> day.spanish_name == '{day.spanish_name}'")


if __name__ == "__main__":
    main(index=1)
