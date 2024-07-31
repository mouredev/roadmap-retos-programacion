"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
"""
'Sin Aplicar'
class Pedido:
    def __init__(self,id:int, productos:list[str,int,int]) -> None:
        self.id = id
        self.productos = productos

    def calcular_total(self):
        total = 0
        for producto,precio,cantidad in self.productos:
            parcial = precio * cantidad
            print(f"{producto} - {precio} * {cantidad} = {parcial}")
            total += parcial
        print(f"\nTotal: {total}")

class PedidoVip(Pedido):
    def __init__(self, id: int, productos: list[str,int,int]) -> None:
        super().__init__(id, productos)

    def calcular_total(self,descuento:float):
        total = 0
        for producto,precio,cantidad in self.productos:
            parcial = precio * cantidad
            print(f"{producto} - {precio} * {cantidad} = {parcial}")
            total += parcial
        print(f"\nTotal: {total / descuento}")

# Prueba
pedido_1 = Pedido(1,[["Pizza", 9.50, 4]])
pedido_vip = PedidoVip(2,[["Pizza Baracoa", 12.50, 2]])
try:
    pedido_1.calcular_total()
    pedido_vip.calcular_total()

except TypeError as e:
    print(f"Error: {e}")

'Aplicado'
class Pedido2:
    def __init__(self,id:int, productos:list[str,int,int]) -> None:
        self.id = id
        self.productos = productos

    def calcular_total(self):
        total = 0
        for producto,precio,cantidad in self.productos:
            parcial = precio * cantidad
            print(f"{producto} - {precio} * {cantidad} = {parcial}")
            total += parcial
        print(f"\nTotal: {total}")
        return total

class Pedido2Vip(Pedido2):
    def __init__(self, id: int, productos: list[str]) -> None:
        super().__init__(id, productos)

    def calcular_total(self):
        total =  super().calcular_total()
        total_descuento = total - total * 0.10
        print(f"Total con descuento Vip (10% = {total * 0.10}): {total_descuento}€")

# Prueba
pedido2_1 = Pedido2(1,[["Pizza", 9.50, 4]])
pedido2_vip = Pedido2Vip(2,[["Pizza Baracoa", 12.50, 2]])
pedido2_1.calcular_total()
pedido2_vip.calcular_total()