# EJERCICIO:
# Explora el "Principio SOLID de Segregación de Interfaces
# (Interface Segregation Principle, ISP)", y crea un ejemplo
# simple donde se muestre su funcionamiento de forma correcta e incorrecta.
from abc import ABC, abstractmethod


# Ejemplo Incorrecto
class MetodoPagoInterface(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        return f"Pago procesado correctamente de ${monto}"

    @abstractmethod
    def reembolsar_pago(self, monto: float):
        return f"Pago reembolsado correctamente de ${monto}"

    @abstractmethod
    def dividir_en_cuotas(self, monto: float, cuotas: int):
        return f"Pago dividido en {cuotas} cuotas de ${monto / cuotas}"


class PagoEfectivo(MetodoPagoInterface):
    def procesar_pago(self, monto: float):
        return f"Pago procesado correctamente de ${monto}"

    def reembolsar_pago(self, monto: float):
        return f"Pago reembolsado correctamente de ${monto}"

    def dividir_en_cuotas(self, monto: float, cuotas: int):  # No se divide en cuotas
        raise NotImplementedError("El efectivo no se divide en cuotas")


class PagoTarjeta(MetodoPagoInterface):
    def procesar_pago(self, monto: float):
        return super().procesar_pago(monto)

    def reembolsar_pago(self, monto: float):
        return super().reembolsar_pago(monto)

    def dividir_en_cuotas(self, monto: float, cuotas: int):
        return super().dividir_en_cuotas(monto, cuotas)


# Ejemplo Correcto
class Pagable(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float):
        return f"Pago procesado por el monto de ${monto}"


class Reembolsable(ABC):
    @abstractmethod
    def reembolsar_pago(self, monto: float):
        return f"Pago reembolsado correctamente por ${monto}"


class Financiable(ABC):
    @abstractmethod
    def dividir_en_cuotas(self, monto: float, cuotas: int):
        return f"Pago dividido en {cuotas} cuotas de ${monto / cuotas}"


class PagoEfectivoV2(Pagable, Reembolsable):
    def procesar_pago(self, monto: float):
        return f"Pago procesado correctamente de ${monto}"

    def reembolsar_pago(self, monto: float):
        return f"Pago reembolsado correctamente de ${monto}"


class PagoTarjetaV2(Pagable, Reembolsable, Financiable):
    def procesar_pago(self, monto: float):
        return super().procesar_pago(monto)

    def reembolsar_pago(self, monto: float):
        return super().reembolsar_pago(monto)

    def dividir_en_cuotas(self, monto: float, cuotas: int):
        return super().dividir_en_cuotas(monto, cuotas)


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
class ImprimibleBlancoNegro(ABC):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
    @abstractmethod
    def imprimir_blanco_negro(self, documento: str):
        return f"[{self.modelo}] Imprimiendo {documento}"


class ImprimibleColor(ABC):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
    @abstractmethod
    def imprimir_color(self, documento: str):
        return f"[{self.modelo}] Imprimiendo ${documento} en color"


class Escaneable(ABC):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
    @abstractmethod
    def escanear(self, documento: str):
        return f"Escaneando ${documento}"


class EnviadorFax(ABC):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
    @abstractmethod
    def enviar_fax(self, documento: str, destino: str):
        return f"Enviando fax ${documento} al destino {destino}"


# implementaciones concretas
# ---------------------------------------------------------------------------
class ImpresoraBlancoNegro(ImprimibleBlancoNegro):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0

    def imprimir_blanco_negro(self, documento: str):
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en blanco y negro (Página #{self.paginas_impresas})"


class ImpresoraColor(ImprimibleColor):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0

    def imprimir_color(self, documento: str):
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

    def imprimir_blanco_negro(self, documento: str):
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en blanco y negro (Página #{self.paginas_impresas})"

    def imprimir_color(self, documento: str):
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en color (Página #{self.paginas_impresas})"

    def escanear(self, documento: str):
        self.paginas_escaneadas += 1
        return f"[{self.modelo}] Escaneando '{documento}' (Página #{self.paginas_escaneadas})"

    def enviar_fax(self, documento: str, destino: str):
        self.paginas_enviadas_fax += 1
        return f"[{self.modelo}] Enviando fax '{documento}' (Página #{self.paginas_enviadas_fax})"


class ImpresoraAvanzadaColor(ImpresoraColor, Escaneable):
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.paginas_impresas = 0
        self.paginas_escaneadas = 0

    def imprimir_color(self, documento: str):
        self.paginas_impresas += 1
        return f"[{self.modelo}] Imprimiendo '{documento}' en color (Página #{self.paginas_impresas})"

    def escanear(self, documento: str):
        self.paginas_escaneadas += 1
        return f"[{self.modelo}] Escaneando '{documento}' (Página #{self.paginas_escaneadas})"


### ================================================ ###
### PRUEBAS
### ================================================ ###


def probar_impresora_bn(impresora: ImprimibleBlancoNegro):
    print(impresora.imprimir_blanco_negro("Documento.pdf"))


def probar_impresora_color(impresora: ImprimibleColor):
    print(f"\nProbando impresora a color: {impresora.modelo}")
    print(f"  {impresora.imprimir_color('presentacion.pptx')}")


def probar_escaner(dispositivo: Escaneable):
    print(f"\nProbando escáner: {dispositivo.modelo}")
    print(f"  {dispositivo.escanear('contrato.pdf')}")


def probar_fax(dispositivo: EnviadorFax):
    print(f"\nProbando fax: {dispositivo.modelo}")
    print(f"  {dispositivo.enviar_fax('documento_urgente.pdf', '+34-123-456-789')}")


def probar_multifuncion(impresora: ImpresoraMultifuncion):
    print(f"\nProbando impresora multifunción: {impresora.modelo}")
    print(f"  {impresora.imprimir_blanco_negro('factura.pdf')}")
    print(f"  {impresora.imprimir_color('foto.jpg')}")
    print(f"  {impresora.escanear('recibo.pdf')}")
    print(f"  {impresora.enviar_fax('orden.pdf', '+34-987-654-321')}")


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
