# 10 Excepciones

# Ejercicio

from datetime import datetime
a = ["hola", 7, 2, 3, 6]
b = []
c = [7, 2, 3, 6]


def calculos(lista, operacion):
    if operacion == "media":
        try:
            media = sum(lista) / len(lista)
            return media
        except Exception as e:
            return f"Ha habido una excepción: {e}"
    elif operacion == "conteo":
        try:
            contar = len(lista)
            return contar
        except Exception as e:
            return f"Ha habido una excepción: {e}"
    elif operacion == "division":
        try:
            dividir = len(lista)/lista[4]
            return dividir
        except Exception as e:
            return f"Ha habido una excepción: {e}"
    else:
        return "Operación no válida."


resultado_media_a = calculos(a, "media")
resultado_media_b = calculos(b, "media")
resultado_media_c = calculos(c, "media")

resultado_conteo_a = calculos(a, "conteo")
resultado_conteo_b = calculos(b, "conteo")
resultado_conteo_c = calculos(c, "conteo")

resultado_division_a = calculos(a, "division")
resultado_division_b = calculos(b, "division")
resultado_division_c = calculos(c, "division")

print(f"Resultado media a: {resultado_media_a}")
print(f"Resultado media b: {resultado_media_b}")
print(f"Resultado media c: {resultado_media_c}")

print(f"Resultado conteo a: {resultado_conteo_a}")
print(f"Resultado conteo b: {resultado_conteo_b}")
print(f"Resultado conteo c: {resultado_conteo_c}")

print(f"Resultado division a: {resultado_division_a}")
print(f"Resultado division b: {resultado_division_b}")
print(f"Resultado division c: {resultado_division_c}")


# Dificultad Extra

class PresionArterialError(Exception):
    pass


def registro_presion_arterial():
    datos = {}
    while True:
        try:

            paciente_id = input("ID del paciente: ")
            if not paciente_id.isdigit():
                raise TypeError("El ID debe ser un número")

            datos['paciente'] = int(paciente_id)
            fecha_str = input("Fecha (dd-mm-yyyy): ")
            datos['fecha'] = datetime.strptime(fecha_str, "%d-%m-%Y")

            datos['presion_alta'] = int(input("Presión arterial alta: "))
            if datos['presion_alta'] < 50 or datos['presion_alta'] > 240:
                raise ValueError(
                    "Error en el registro del dato de presion alta")

            datos['presion_baja'] = int(input("Presión arterial baja: "))
            if datos['presion_baja'] < 45 or datos['presion_baja'] > 120:
                raise PresionArterialError(
                    "La presión arterial baja debe estar entre 45 y 120")
            break
        except (ValueError, PresionArterialError, TypeError) as e:
            print(f"{type(e).__name__}: {e}. Intente nuevamente.")
    print("Carga de datos finalizada.")
    return datos


try:
    datos = registro_presion_arterial()
    print("\nDatos del paciente:")
    print(f"ID: {datos['paciente']}")
    print(f"Fecha de la toma: {datos['fecha'].strftime('%d-%m-%Y')}")
    print(f"Presión arterial alta: {datos['presion_alta']}")
    print(f"Presión arterial baja: {datos['presion_baja']}")
    print("No se ha producido ningún error.")
except Exception as e:
    print(f"{type(e).__name__}: {e}.")
finally:
    print("La ejecución ha finalizado.")
