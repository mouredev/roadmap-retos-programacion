import asyncio
from random import randint

plates = []
tasks = []


class Plate:
    id: int
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name


async def confirmation(data: (int, str)):
    await asyncio.sleep(randint(1, 10))
    print(f"\n✅ Plato {data[0]} preparado\n")


async def create_plate(callback, plate_data: (int, str)):
    plate = Plate(plate_data[0], plate_data[1])
    plates.append(plate)
    print("Plato en preparación")
    task = asyncio.create_task(callback(plate_data))
    tasks.append(task)


def plate_given(id: int):
    given = False
    for plate in plates:
        if plate.id == id:
            plates.remove(plate)
            print("Plato entregado")
            given = True
            break

    if not given:
        print("❌ Plato no encontrado")


async def async_input(prompt):
    return await asyncio.to_thread(input, prompt)


async def main():
    exit = False

    while not exit:
        print("\nSelecciona una opción:\n"
              "1 - Introduce plato:\n"
              "2 - Indicar plato entregado\n"
              "3 - Salir")
        choice = int(await async_input("> "))

        if choice == 1:
            plate_name = input("Nombre del plato: ")
            plate_id = len(plates) + 1
            await create_plate(confirmation, (plate_id, plate_name))
        elif choice == 2:
            id = int(input("ID del plato: "))
            plate_given(id)
        elif choice == 3:
            print("Hasta pronto 👋")
            exit = True
        else:
            print("⚠️ Opción errónea")

    # Espera a que todas las tareas se hayan completado antes de terminar
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
