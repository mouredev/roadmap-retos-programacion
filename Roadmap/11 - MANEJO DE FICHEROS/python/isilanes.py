"""
El enunciado del ejercicio extra es confuso. Parece desearse un listado de ventas, en el que cada
entrada/línea sea una VENTA. Sin embargo, el enunciado dice "Cada PRODUCTO se guarda en una línea
del arhivo (sic), de la siguiente manera [...]". Si vendo 2 manzanas un día, y 3 otro, ¿la segunda
venta debe ir en una línea adicional, o debo actualizar la primera línea, y cambiar el 2 por un 5?

La respuesta obvia parece ser la primera opción, y asumir que cada línea es una VENTA, no un PRODUCTO.
Si esto es así, también es confusa la opción de "eliminar productos" que menciona el enunciado.
¿Se refiere a eliminar ventas? ¿O son realmente productos? En el segundo caso habría que borrar todas
las líneas con ventas de un determinado producto. Asumo la opción más obvia, que cada línea
es una venta, y que las entradas añadidas/modificadas/eliminadas son ventas (no productos).
"""
from pathlib import Path


class Lock:
    """
    Class to lock a file, so that multiple concurrent executions do not clash.
    """
    def __init__(self, file: Path):
        self.file = file

    @property
    def lock(self) -> Path:
        lock_name = f".{self.file.name}.lock"

        return self.file.parent.joinpath(lock_name)

    def __enter__(self):
        if self.lock.exists():  # then someone else acquired the lock already
            return None

        self.lock.touch()

        return self.lock

    def __exit__(self, *args, **kwargs):
        self.lock.unlink(missing_ok=True)


def main():
    file = Path("./isilanes.txt")
    file.write_text("Iñaki Silanes\n46 años\nPython\n")

    contents = file.read_text()
    print(contents, end="")

    file.unlink()


def extra():
    db_file = Path("./ventas.txt")

    while True:
        # Si no quisiera limitarme a las librerías estándar, recomiendo mucho Questionary,
        # para interacción por CLI.
        option = input("Selecciona: [a]ñadir, [c]onsultar, ac[t]ualizar, [e]liminar, [v]entas totales, ve[n]tas por producto, [s]alir: ")

        if option == "a":
            add_sale(db_file)

        elif option == "c":
            check_sales(db_file)

        elif option == "t":
            update_sale(db_file)

        elif option == "e":
            remove_sale(db_file)

        elif option == "v":
            print_total_sales(db_file)

        elif option == "n":
            print_sales_per_product(db_file)

        elif option == "s":
            break

    # On exit, delete db file:
    db_file.unlink(missing_ok=True)


def add_sale(db_file: Path) -> bool:
    """
    Add the data for one sale.

    Args:
        db_file (Path):
            Text file with sales "database".

    Returns:
        True if data insertion was successful, False otherwise.
    """
    name = input("Nombre del producto: ")

    units = input("Unidades vendidas: ")
    try:
        units = int(units)
    except ValueError:
        print("Debes introducir un número entero. Abortando...")
        return False

    price = input("Precio unitario: ")
    try:
        price = float(price)
    except ValueError:
        print("Debes introducir un número. Abortando...")
        return False

    with Lock(db_file) as lock:
        if not lock:
            print(f"No pudimos bloquear el fichero '{db_file}'. Algún otro proceso debe de estar usándolo.")
            return False

        line = f"{name}, {units}, {price}\n"

        with open(db_file, "a", encoding="utf-8") as f:
            f.write(line)

    return True


def check_sales(db_file: Path) -> None:
    """
    List all sales so far. In other words, print the contents of the db file.
    If the db file does not exist, do nothing.

    Args:
         db_file (Path):
            Text file with sales "database".

    Returns:
        Nothing.
    """
    if not db_file.exists():
        return

    print("Ventas recogidas en la base de datos:")
    print(db_file.read_text(), end="")


def update_sale(db_file: Path) -> bool:
    """
    Update an existing sale.
    If the db file does not exist, do nothing.

    Args:
         db_file (Path):
            Text file with sales "database".

    Returns:
        True if update was successful, False otherwise.
    """
    if not db_file.exists():
        return False

    with Lock(db_file) as lock:
        if not lock:
            print(f"No pudimos bloquear el fichero '{db_file}'. Algún otro proceso debe de estar usándolo.")
            return False

        sales = []
        with open(db_file, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                print(f"{i:3d}: {line}", end="")
                sales.append(line)

        index = input("Escoge una venta a modificar, por índice (Enter sin número para cancelar): ")

        if index == "":
            return False

        try:
            index = int(index)
            line = sales[index]
        except ValueError:
            print("El índice no es un número entero. Abortando...")
            return False
        except IndexError:
            print("Índice fuera de los valores posibles. Abortando...")
            return False

        name, units, price = line.split(",")
        units = int(units)
        price = float(price)

        which = input("¿Qué campo quieres modificar? ([n]ombre, [c]antidad, [p]recio): ")

        if which == "n":
            new = input("Nuevo nombre del producto: ")
            name = new
        elif which == "c":
            new = input("Nueva cantidad de producto: ")
            units = int(new)
        elif which == "p":
            new = input("Nuevo precio del producto: ")
            price = float(new)

        sales[index] = f"{name}, {units}, {price}\n"
        with open(db_file, "w", encoding="utf-8") as f:
            for sale in sales:
                f.write(sale)

    return True


def remove_sale(db_file: Path) -> bool:
    """
    Remove an existing sale.
    If the db file does not exist, do nothing.

    Args:
         db_file (Path):
            Text file with sales "database".

    Returns:
        True if removal was successful, False otherwise.
    """
    if not db_file.exists():
        return False

    with Lock(db_file) as lock:
        if not lock:
            print(f"No pudimos bloquear el fichero '{db_file}'. Algún otro proceso debe de estar usándolo.")
            return False

        sales = []
        with open(db_file, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                print(f"{i:3d}: {line}", end="")
                sales.append(line)

        index = input("Escoge una venta a eliminar, por índice (Enter sin número para cancelar): ")

        if index == "":
            return False

        try:
            index = int(index)
        except ValueError:
            print("El índice no es un número entero. Abortando...")
            return False

        sales = sales[:index] + sales[index+1:]
        with open(db_file, "w", encoding="utf-8") as f:
            for sale in sales:
                f.write(sale)

    return True


def print_total_sales(db_file: Path) -> None:
    """
    Print out the total sales.
    If the db file does not exist, do nothing.

    Args:
         db_file (Path):
            Text file with sales "database".

    Returns:
        Nothing.
    """
    if not db_file.exists():
        return

    total_sold = 0
    with open(db_file, "r", encoding="utf-8") as f:
        for line in f:
            _, units, price = line.split(",")
            units = int(units)
            price = float(price)
            total_sold += units * price

    print(f"Volumen de ventas total: {total_sold:.2f}")


def print_sales_per_product(db_file: Path) -> None:
    """
    Print out the sales per product.
    If the db file does not exist, do nothing.

    Args:
         db_file (Path):
            Text file with sales "database".

    Returns:
        Nothing.
    """
    if not db_file.exists():
        return

    sales = {}
    with open(db_file, "r", encoding="utf-8") as f:
        for line in f:
            prod, units, price = line.split(",")
            units = int(units)
            price = float(price)
            sales[prod] = {
                "units": sales.get(prod, {}).get("units", 0) + units,
                "volume": sales.get(prod, {}).get("volume", 0) + units*price,
            }

    print("Ventas totales por producto:")
    for k, v in sales.items():
        print(f"{k:10s}: {v.get('units', 0):2d} unidades, {v.get('volume', 0):6.2f} volumen total")


if __name__ == "__main__":
    main()
    extra()
