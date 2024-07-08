def bill_amount(amount: float, tax_rate: float = 21.0, book: str = "default_book.log") -> float:
    total_amount = amount * (1 + tax_rate / 100)

    print(f"Facturamos {total_amount:.2f} eur ({amount:.2f} + tasas) en '{book}'")


def get_taxable_data(amount: float, tax_rate: float = 21.0) -> dict:
    taxes = amount * tax_rate / 100

    return {
        "base": amount,
        "taxes": taxes,
        "total": amount + taxes,
    }


def save_bill(taxable: dict, book: str = "default_book.log"):
    base = taxable.get("base")
    total = taxable.get("total")
    if not base or not total:
        return

    print(f"Facturamos {total:.2f} eur ({base:.2f} + tasas) en '{book}'")


def main():
    print("===== MAIN =====")
    print("Con la implementación no-SRP, tenemos una función que hace dos cosas:")
    print("1. calcula los impuestos")
    print("2. guarda la factura.")
    print(">>> bill_amount(100, 21)")
    bill_amount(100, 21)

    print("\nAquí el problema es que tendremos que modificar bill_amount() en dos circunstancias:")
    print("1. Si se modifica algo relativo a cómo se calculan los impuestos (por ejemplo,")
    print("   que en lugar de aplicar un porcentaje fijo, se sume una constante, o que")
    print("   el procentaje dependa de la cantidad base).")
    print("2. Si se modifica algo relacionado con cómo se guarda la factura (por ejemplo,")
    print("   que en lugar de guardar la factura en un archivo, se guarde en una base de datos,")
    print("   o que se quiera guardar la información en otro formato).")

    print("\nCon una implementación SRP, hemos separado las dos responsabilidades en dos funciones:")
    print('taxable_data = get_taxable_data(250, 15)')
    print('save_bill(taxable_data)')
    taxable_data = get_taxable_data(250, 15)
    save_bill(taxable_data)

    print("\nDe esta manera, si el cálculo de los impuestos cambia, sólo tendremos que modificar la")
    print("función get_taxable_data(). Por otro lado, si se quiere cambiar cómo se guarda la factura,")
    print("sólo tendremos que modificar la función save_bill().")
    print("El único requisito común es que ambas funciones respeten el contrato de que get_taxable_data()")
    print("devuelva un diccionario compatible con lo que save_bill() espera. En un caso real, podríamos usar")
    print("una clase ad hoc para esto, y forzar que una función devuelva un objeto de esa clase, y la otra lo use.")


if __name__ == "__main__":
    main()
