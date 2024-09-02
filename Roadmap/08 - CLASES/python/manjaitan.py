class coche:

    def __init__(self, marca, modelo, color) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def imprimir (self):
        print (
            f"Marca: {self.marca} | Modelo: {self.modelo} | Color: {self.color}")



coche1 = coche("Ford" , "Escort" , "Rojo")
coche1.imprimir()
# modifico el parametro color
coche1.color = "Verde"
coche1.imprimir()


#### EXTRA ####

