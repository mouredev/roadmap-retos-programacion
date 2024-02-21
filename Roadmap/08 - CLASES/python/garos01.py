# Clases


class Vehiculo:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def imprimir_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")


# Crear una instancia de la clase Vehiculo
vehiculo1 = Vehiculo(marca="Toyota", modelo="Camry", anio=2022, color="Azul")

# Imprimir la información inicial
print("Información inicial del vehículo:")
vehiculo1.imprimir_informacion()

# Modificar algunos atributos
vehiculo1.anio = 2023
vehiculo1.color = "Rojo"

# Imprimir la información después de la modificación
print("\nInformación después de la modificación:")
vehiculo1.imprimir_informacion()

# Ejercicio extra


class Impresora:
    def __init__(self):
        self.cola_impresion = []

    def recibir_documento(self, documento):
        self.cola_impresion.append(documento)
        print("Documento recibido:", documento)

    def imprimir(self):
        if self.cola_impresion:
            documento_a_imprimir = self.cola_impresion.pop(0)
            print("Imprimiendo documento:", documento_a_imprimir)
        else:
            print("No hay documentos en la cola de impresión")


impresora = Impresora()

impresora.recibir_documento("Documento1.txt")
impresora.recibir_documento("Documento2.pdf")
impresora.recibir_documento("Documento3.doc")

impresora.imprimir()
impresora.imprimir()
impresora.imprimir()
impresora.imprimir()
