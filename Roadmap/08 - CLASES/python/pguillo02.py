class Animal:
    def __init__(self, tipo: str, altura: int):
        self.__tipo = tipo
        self.__altura = altura

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, new_tipo):
        self.__tipo = new_tipo

    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self, new_altura):
        self.__altura = new_altura
    
    def __str__(self):
        return f"Este es una animal de tipo {self.tipo} y de altura {self.altura}"

ejemplo = Animal("mamífero", 3)
print(ejemplo)

    

