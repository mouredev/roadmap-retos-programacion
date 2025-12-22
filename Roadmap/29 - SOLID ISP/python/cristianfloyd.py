# EJERCICIO:
# Explora el "Principio SOLID de Segregación de Interfaces
# (Interface Segregation Principle, ISP)", y crea un ejemplo
# simple donde se muestre su funcionamiento de forma correcta e incorrecta.
from abc import ABC, abstractmethod


# Ejemplo Incorrecto
class MetodoPagoInterface(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        pass

    @abstractmethod
    def reembolsar_pago(self, monto: float) -> str:
        pass

    @abstractmethod
    def dividir_en_cuotas(self, monto: float, cuotas: int) -> str:
        pass


class PagoEfectivo(MetodoPagoInterface):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago procesado correctamente de ${monto}"

    def reembolsar_pago(self, monto: float) -> str:
        return f"Pago reembolsado correctamente de ${monto}"

    def dividir_en_cuotas(self, monto: float, cuotas: int) -> str:  # No se divide en cuotas
        raise NotImplementedError("El efectivo no se divide en cuotas")


class PagoTarjeta(MetodoPagoInterface):
    def procesar_pago(self, monto: float) -> str:
        return f"Pago procesado correctamente de ${monto}"

    def reembolsar_pago(self, monto: float) -> str:
        return f"Pago reembolsado correctamente de ${monto}"

    def dividir_en_cuotas(self, monto: float, cuotas: int) -> str:
        return f"Pago dividido en {cuotas} cuotas de ${monto / cuotas}"


# Ejemplo Correcto
class Pagable(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> str:
        pass


class Reembolsable(ABC):
    @abstractmethod
    def reembolsar_pago(self, monto: float) -> str:
        pass


class Financiable(ABC):
    @abstractmethod
    def dividir_en_cuotas(self, monto: float, cuotas: int) -> str:
        pass


class PagoEfectivoV2(Pagable, Reembolsable):
    def procesar_pago(self, monto: float):
        return f"Pago procesado correctamente de ${monto}"

    def reembolsar_pago(self, monto: float):
        return f"Pago reembolsado correctamente de ${monto}"


class PagoTarjetaV2(Pagable, Reembolsable, Financiable):
    def procesar_pago(self, monto: float):
        return f"Pago procesado correctamente de ${monto}"

    def reembolsar_pago(self, monto: float):
        return f"Pago reembolsado correctamente de ${monto}"

    def dividir_en_cuotas(self, monto: float, cuotas: int):
        return f"Pago dividido en {cuotas} cuotas de ${monto / cuotas}"


class PagoCriptomoneda(Pagable):
    def procesar_pago(self, monto: float):
        return f"Pago procesado correctamente en criptomoneda de ${monto}"


# DIFICULTAD EXTRA (opcional):
# Crea un gestor de impresoras.
# Requisitos:
# 1. Algunas impresoras sólo imprimen en blanco y negro.
# 2. Otras sólo a color.
# 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
# Instrucciones:
# 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
# 2. Aplica el ISP a la implementación.
# 3. Desarrolla un código que compruebe que se cumple el principio.


# Interfaces segregadas
class DispositivoIdentificable(ABC):
    @abstractmethod
    def get_modelo(self) -> str:
        pass

class ImprimibleBlancoNegro(DispositivoIdentificable):

    @abstractmethod
    def imprimir_blanco_negro(self, documento: str) -> str:
        pass


class ImprimibleColor(DispositivoIdentificable):

    @abstractmethod
    def imprimir_color(self, documento: str) -> str:
        pass


class Escaneable(DispositivoIdentificable):
    
    @abstractmethod
    def escanear(self, documento: str) -> str:
        pass


class EnviadorFax(DispositivoIdentificable):
    
    @abstractmethod
    def enviar_fax(self, documento: str, destino: str) -> str:
        pass



# implementaciones concretas
# ---------------------------------------------------------------------------
class ImpresoraBlancoNegro(ImprimibleBlancoNegro):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0

    def get_modelo(self) -> str:
        return self.modelo

    def imprimir_blanco_negro(self, documento: str) -> str:
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en blanco y negro (Página #{self.paginas_impresas})"


class ImpresoraColor(ImprimibleColor):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0

    def get_modelo(self) -> str:
        return self.modelo

    def imprimir_color(self, documento: str) -> str:
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en color (Página #{self.paginas_impresas})"


class ImpresoraMultifuncion(
    ImprimibleBlancoNegro, ImprimibleColor, Escaneable, EnviadorFax
):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0
        self.paginas_escaneadas = 0
        self.paginas_enviadas_fax = 0

    def get_modelo(self) -> str:
        return self.modelo

    def imprimir_blanco_negro(self, documento: str) -> str:
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en blanco y negro (Página #{self.paginas_impresas})"

    def imprimir_color(self, documento: str) -> str:
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en color (Página #{self.paginas_impresas})"

    def escanear(self, documento: str) -> str:
        self.paginas_escaneadas += 1
        return f"[{self.modelo}] Escaneando '{documento}' (Página #{self.paginas_escaneadas})"

    def enviar_fax(self, documento: str, destino: str) -> str:
        self.paginas_enviadas_fax += 1
        return f"[{self.modelo}] Enviando fax '{documento}' (Página #{self.paginas_enviadas_fax})"


class ImpresoraAvanzadaColor(ImprimibleColor, Escaneable):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0
        self.paginas_escaneadas = 0

    def get_modelo(self) -> str:
        return self.modelo

    def imprimir_color(self, documento: str) -> str:
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en color (Página #{self.paginas_impresas})"

    def escanear(self, documento: str) -> str:
        self.paginas_escaneadas += 1
        return f"[{self.modelo}] Escaneando '{documento}' (Página #{self.paginas_escaneadas})"


### ================================================ ###
### PRUEBAS
### ================================================ ###


def probar_impresora_bn(impresora: ImprimibleBlancoNegro):
    print(f"\n Probando impresora BN: {impresora.get_modelo()}")
    print(impresora.imprimir_blanco_negro("Documento.pdf"))


def probar_impresora_color(impresora: ImprimibleColor):
    print(f"\nProbando impresora a color: {impresora.get_modelo()}")
    print(impresora.imprimir_color('presentacion.pptx'))


def probar_escaner(dispositivo: Escaneable):
    print(f"\nProbando escáner: {dispositivo.get_modelo()}")
    print(dispositivo.escanear('contrato.pdf'))


def probar_fax(dispositivo: EnviadorFax):
    print(f"\nProbando fax: {dispositivo.get_modelo()}")
    print(dispositivo.enviar_fax('documento_urgente.pdf', '+34-123-456-789'))


def probar_multifuncion(impresora: ImpresoraMultifuncion):
    print(f"\nProbando impresora multifunción: {impresora.get_modelo()}")
    print(f"  {impresora.imprimir_blanco_negro('factura.pdf')}")
    print(impresora.imprimir_color('foto.jpg'))
    print(impresora.escanear('recibo.pdf'))
    print(impresora.enviar_fax('orden.pdf', '+34-987-654-321'))


hp_laserjet = ImpresoraBlancoNegro("HP LaserJet Pro")
epson_colorjet = ImpresoraColor("Epson EcoTank Color")
canon_multifuncion = ImpresoraMultifuncion("Canon PIXMA MX922")
brother_avanzada = ImpresoraAvanzadaColor("Brother MFC-J995DW")

print("\nProbando impresora blanco y negro:")
probar_impresora_bn(hp_laserjet)
probar_impresora_bn(canon_multifuncion) 

print("\nProbando impresora a color:")
probar_impresora_color(epson_colorjet)
probar_impresora_color(canon_multifuncion)
probar_impresora_color(brother_avanzada)

print("\nProbando escáner:")
probar_escaner(canon_multifuncion)
probar_escaner(brother_avanzada)

print("\nProbando fax:")
probar_fax(canon_multifuncion)

print("\nProbando multifunción:")
probar_multifuncion(canon_multifuncion)
