from enum import Enum


# EJERCICIO 1

class DiasSemana(Enum):
    """Enumera Dias de la semana"""
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7
    
    
def obtener_dia_semana():
        while True:
            try:
                numero = int(input("Ingrese el numero del dia de la semana: "))
                
                if numero < 1 or numero > 7:
                    print("Numero del dia de la semana incorrecto, debe ser en el rango de 1 a 7")
                    continue
                
                mensaje = f"El dia de la semana es: {DiasSemana(numero).name.capitalize()}"
    
                print(mensaje)
                
                break
            
            except ValueError:
                print("Debe ser un numero entero en el rango del 1 - 7")
                continue


# ------------------------------------------------------#


# EJERCICIO 2

class EstadoPedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4


class Pedido:
    def __init__(self, identificador):
        # Genera un identificador
        self.identificador = identificador
        self.estado = EstadoPedido.PENDIENTE
    
    def enviar_pedido(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print(f"El pedido {self.identificador} ya ha sido enviado")
        
        elif self.estado == EstadoPedido.ENVIADO:
            print(f"El pedido {self.identificador} ya fue enviado")
        
        elif self.estado == EstadoPedido.CANCELADO:
            print(f"El pedido {self.identificador} ya fue cancelado")
        
        elif self.estado == EstadoPedido.ENTREGADO:
            print(f"El pedido {self.identificador} ya fue entregado")
                            
    
    def cancelar_pedido(self):
        if self.estado == EstadoPedido.PENDIENTE or self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.CANCELADO
            print(f"El pedido {self.identificador} ha sido cancelado")
            
        elif self.estado == EstadoPedido.ENTREGADO:
            print(f"No se puede cancelar el pedido {self.identificador} por que ya se entrego")
            
        elif self.estado == EstadoPedido.CANCELADO:
            print(f"El pedido {self.identificador} ya fue cancelado")
            
    
    def entregar_pedido(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estadio = EstadoPedido.ENTREGADO
            print(f"El pedido {self.identificador} fue entregado")
        
        elif self.estado == EstadoPedido.PENDIENTE:
            print(f"El pedido {self.identificador} aun esta pendiente")    
        
        elif self.estado == EstadoPedido.ENTREGADO:
            print(f"El pedido {self.identificador} ya fue entregado")
        
        elif self.estado == EstadoPedido.CANCELADO:
            print(f"El pedido {self.identificador} ya fue cancelado")



if __name__ == "__main__":
    # Ejemplo de uso del ejercicio 1:
    obtener_dia_semana()
    
    
    # --------------------------------#
    
    
    # Ejemplos de uso dle ejercicio 2:
    pedido_1 = Pedido(identificador=1)
    pedido_2 = Pedido(identificador=2)


    pedido_1.enviar_pedido()
    pedido_1.cancelar_pedido()
    pedido_1.entregar_pedido()

    pedido_2.cancelar_pedido()
    pedido_2.entregar_pedido()
    pedido_2.enviar_pedido()   