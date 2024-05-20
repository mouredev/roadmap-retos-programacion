### Clases ###

class MiClasePersona:
    def __init__(self, nombre:str, apellido:str) -> None:
        self.nombre = nombre
        self.apellido = apellido
    
    def imprimir_atributos(self) -> None:
        print(f'Atributos de la clase: \n[{self.nombre} - {self.apellido}]')
    
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Apellido: {self.apellido}'
    
# Inicializando la clase

mi_clase_persona = MiClasePersona('Javier', 'Molina')

mi_clase_persona.imprimir_atributos() # Llamando una funcion
print(mi_clase_persona) # Por defecto se llama la funcion __str__ al imprimir el objeto


